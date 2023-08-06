# Flask-Bpjs

Blah blah blah.

## Compatability
Python 3.6+ is required.

## Installation

```bash
pip install Flask-Bpjs

## Quickstart
1. Import with ```from flask_bpjs import FlaskBpjs```
```python
# example.py
from flask import Flask
from flask_bpjs import FlaskBpjs

app = Flask(__name__)
ext=FlaskBpjs(consid='BPJS_CONST_ID',user_key='BPJS_USER_KEY',secret_key='BPJS_SECRET_KEY',host='BPJS_HOST')
ext.init_app(app)


if __name__ == '__main__':
    app.run()
```
Running the example:
```bash
python example.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```