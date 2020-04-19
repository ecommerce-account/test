# -*- coding: utf-8 -*-

import stripe
from flask import render_template, Flask, request

app = Flask(__name__)

STRIPE_SECRET_KEY="sk_test_si9qlwJI4IVNf29PbhwA6sKA00KWtNmD1B"

stripe.api_key = STRIPE_SECRET_KEY
@app.route('/')
def hello_world():
    return render_template('item.html')

@app.route('/charge', methods=['POST'])
def charge():
    user_email = request.form["email"]
    try:
        amount = 70
        customer = stripe.Customer.create(
            email=user_email,
            source=request.form['stripeToken']
        )
        stripe.Charge.create(
            customer=customer.id,
            amount=amount,
            currency='jpy',
            description='商店のおすすめ品（PythonAnywhere）',
            receipt_email=user_email,
        )
        return render_template('charge.html', amount=amount)
    except stripe.error.StripeError:
        return render_template('error.html')
