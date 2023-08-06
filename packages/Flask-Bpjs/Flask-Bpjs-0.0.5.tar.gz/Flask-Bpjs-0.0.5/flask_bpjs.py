# !/usr/bin/env python3
# encoding: utf-8
import base64
import hashlib
import hmac
import json
import logging
import os
import traceback
from datetime import datetime
from typing import Optional

import lzstring
import requests
from Crypto.Cipher import AES
from requests.structures import CaseInsensitiveDict

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack
logger = logging.getLogger(__name__)
prefix = os.path.basename(__file__)[:-3].lower()


class BpjsSession(object):
    _default_headers = requests.structures.CaseInsensitiveDict({
        'accept': '*/*',
        'upgrade-insecure-requests': '1',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50",
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
    })

    def __init__(self, cons_id, secret_key, user_key,
                 base_url='https://apijkn-dev.bpjs-kesehatan.go.id/vclaim-rest-dev'):
        self.headers = self._default_headers
        self.session = requests.session()
        self._cons_id = cons_id
        self._secret_key = secret_key
        self._user_key = user_key
        self._base_url = base_url

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)

    @property
    def base_url(self) -> Optional[str]:
        return self._base_url

    @property
    def cons_id(self) -> Optional[str]:
        return self._cons_id

    @property
    def secret_key(self) -> Optional[str]:
        return self._secret_key

    @property
    def user_key(self) -> Optional[str]:
        return self._user_key

    @staticmethod
    def decompress(keys, encrypts):
        decompress = None
        try:
            lz = lzstring.LZString()
            key_hash = hashlib.sha256(keys.encode('utf-8')).digest()
            decryptor = AES.new(key_hash[0:32], AES.MODE_CBC, IV=key_hash[0:16])
            plain = decryptor.decrypt(base64.b64decode(encrypts))
            decompress = json.loads(lz.decompressFromEncodedURIComponent(plain.decode('utf-8')))
        except Exception as error:
            logging.exception(error.__str__())
        return decompress

    @staticmethod
    def get_timestamp() -> Optional[str]:
        return str(int(datetime.today().timestamp()))

    @staticmethod
    def get_timetoday() -> Optional[str]:
        return str(datetime.today().strftime('%Y-%m-%d'))

    def get_signature(self) -> tuple:
        time_stamp = self.get_timestamp()
        msg = '{}&{}'.format(self.cons_id, time_stamp)
        signature = hmac.new(bytes(self.secret_key, 'UTF-8'), bytes(msg, 'UTF-8'), hashlib.sha256).digest()
        encoded = base64.b64encode(signature)
        return time_stamp, encoded.decode('UTF-8')

    def request(self, method, path: str, params=None, data=None, files=None, extra_headers=None, timeout=10):
        headers = self.headers.copy()
        time_stamp, signature = self.get_signature()
        decompress_key = ''.join(map(str, [self.cons_id, self.secret_key, time_stamp]))
        headers.update({
            'x-cons-id': self.cons_id,
            'x-timestamp': time_stamp,
            'x-signature': signature,
            'user_key': self.user_key,
        })
        url = '{}/{}'.format(self.base_url.rstrip('/'), path.lstrip('/'))
        if extra_headers is not None:
            for h in extra_headers:
                headers.update([(h, extra_headers[h])])
        decompress = 'SEP/2.0/delete' not in url or "SEP/2.0/update" not in url
        response = self.session.request(method, url, params=params, data=data, timeout=timeout,
                                        headers=headers, files=files, allow_redirects=True)
        response.raise_for_status()
        response.encoding = 'utf-8'
        dict_response = response.json()
        if decompress:
            dict_response.update(response=self.decompress(decompress_key, dict_response.get('response')))
        return dict_response.get('response')

    def get(self, path, params=None):
        try:
            return self.request(path=path, method='GET', params=params)
        except requests.RequestException as error:
            logging.exception(
                ''.join(traceback.format_exception(type(error), value=error, tb=error.__traceback__)))
        return None

    def get_peserta_nik(self, num: str):
        return self.get('peserta/nik/{}/tglsep/{}'.format(num, self.get_timetoday()))

    def get_peserta_nokartu(self, num: str):
        return self.get('peserta/nokartu/{}/tglsep/{}'.format(num, self.get_timetoday()))


class FlaskBpjs(object):
    _bpjs = None
    bpjs_host = None
    bpjs_consid = None
    bpjs_secret_key = None
    bpjs_user_key = None

    def __init__(self, app=None, consid=None, user_key=None, secret_key=None, host=None):
        self.app = app
        self.bpjs_consid = consid
        self.bpjs_secret_key = secret_key
        self.bpjs_user_key = user_key
        self.bpjs_host = host
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.extensions[prefix] = self
        if app.config.get('BPJS_HOST'):
            self.bpjs_host = app.config.get('BPJS_HOST')
        if app.config.get('BPJS_CONST_ID'):
            self.bpjs_consid = app.config.get('BPJS_CONST_ID')
        if app.config.get('BPJS_SECRET_KEY'):
            self.bpjs_secret_key = app.config.get('BPJS_SECRET_KEY')
        if app.config.get('BPJS_USER_KEY'):
            self.bpjs_user_key = app.config.get('BPJS_USER_KEY')
        if self.bpjs_consid is not None and self.bpjs_user_key is not None and self.bpjs_secret_key is not None:
            self._bpjs = BpjsSession(cons_id=self.bpjs_consid, secret_key=self.bpjs_secret_key,
                                     user_key=self.bpjs_user_key,
                                     base_url=self.bpjs_host)
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def teardown(self, exception):
        ctx = stack.top

    def connect(self):
        if self.bpjs_consid is not None and self.bpjs_user_key is not None and self.bpjs_secret_key is not None:
            self._bpjs = BpjsSession(cons_id=self.bpjs_consid, secret_key=self.bpjs_secret_key,
                                     user_key=self.bpjs_user_key,
                                     base_url=self.bpjs_host)
        return self._bpjs

    @property
    def bpjs(self) -> Optional[BpjsSession]:
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'bpjs'):
                ctx.bpjs = self.connect()
            return ctx.bpjs
