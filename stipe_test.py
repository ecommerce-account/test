import stripe
# Set your secret key. Remember to switch to your live secret key in production!
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = 'sk_test_si9qlwJI4IVNf29PbhwA6sKA00KWtNmD1B'

stripe.PaymentIntent.create(
  amount=1000,
  currency='jpy',
  payment_method_types=['card'],
  receipt_email='jenny.rosen@example.com',
)