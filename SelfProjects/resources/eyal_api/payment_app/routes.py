import flask
import random
import datetime
import flask_login
from werkzeug import security
import re
from payment_app import app

@app.route('/')
def home():
    return "Hello!"

@app.route("/api/creditcard", methods=('GET','POST',))
def fake_paypal():

    if flask.request.method == 'GET':
        return "Run me with post method with the following arguments:\ncard_n (card number)\ncvv \
    (cvv code)\nexp (expiration date)\ncost (price to pay), name (user's name)"
    for word in 'card_n exp cvv cost name'.split():
        try:
            assert flask.request.form.get(word)
        except AssertionError:
            print("Problem on:",word)
            return "Bad request", 400

    responses = [
        {
            'valid': True,
            'Payment': flask.request.form.get('cost')
        },
        {
            'valid':False,
            'Payment': flask.request.form.get('cost')
        },
    ]

    return flask.jsonify(random.choice(responses))
