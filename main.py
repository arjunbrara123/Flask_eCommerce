#! /usr/bin/env python3.6
"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
from os import environ
from flask import Flask, jsonify, request, url_for, render_template
import stripe
# This is your real test secret API key.
stripe.api_key = environ['STRIPE_API_KEY']
app = Flask(__name__,
            static_url_path='',
            static_folder='.')
YOUR_DOMAIN = 'http://127.0.0.1:5000/'

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/create-checkout-session', methods=['GET', 'POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 2000,
                        'product_data': {
                            'name': 'Stubborn Attachments',
                            'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=url_for('success'),
            cancel_url=url_for('cancel')
        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route('/')
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
