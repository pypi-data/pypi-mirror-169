# Flask-Telebot

A simple way to demo Flask apps from your machine.
Makes your [Flask](http://flask.pocoo.org/) apps running on localhost available
 over the internet via the excellent [ngrok](https://ngrok.com/) tool.

## Compatability
Python 3.6+ is required.

## Installation

```bash
pip install Flask-Telebot
```
### Inside Jupyter / Colab Notebooks
Notebooks have [an issue](https://stackoverflow.com/questions/51180917/python-flask-unsupportedoperation-not-writable) with newer versions of Flask, so force an older version if working in these environments.
```bash
!pip install flask==0.12.2
```
See the [example notebook](https://colab.research.google.com/github/GatLab/Flask-Telebot/blob/master/examples/example.ipynb) for a working example.

## Quickstart
1. Import with ```from flask_telebot import FlaskTelebot```
```python
# example.py
from flask import Flask
from flask_telebot import FlaskTelebot

app = Flask(__name__)
tele=FlaskTelebot(token='TELEGRAM_BOT_TOKEN')
tele.init_app(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
```
Running the example:
```bash
python example.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Running on http://<random-address>.ngrok.io
```