from flask import jsonify

@app.route('/secret')
def secret():
  intent = # ... Create or retrieve the PaymentIntent
  return jsonify(client_secret=intent.client_secret)
