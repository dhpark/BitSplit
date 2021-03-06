# Credit Card Banking INFO
# Account number:
# 792291319682
# Routing number:
# 325272063
# Credit card

# Credit card number:
# 4032030690230678
# Credit card type:
# Visa
# Expiration date:
# 4/2020
# PayPal

# Balance:
# 9999.00 USD

# #PayPal Info
# PayPal payment card

# Payment card:
# 6221194887829340
# Exp date:
# 06/2018
# Track 1:
# %B6221194887829340^^1805^1010?
# Track 2:
# ;6221194887829340=18051010?


# Balance:
# 23123.00 USD
import paypalrestsdk
from paypalrestsdk import Payment
import logging

logging.basicConfig(level=logging.INFO)
paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "Ac0V2MLPF7brDffSLgf8BnKVSRtuv0XnyfrQt1lIOuYbG9Zt1_AU0t3-u0v3QBNEFmfsHwn1QBfTejwH",
  "client_secret": "EPF_K2Gm8yfnylElN5XWsp6d-FufdHIzB5sGoS_X81tKp16s60-7Dl4wOXdcE0niKQe8MsSbirCKKczF" })

amount = input('Enter the amount of your donation: ')
print(amount)
amount = "%.2f" % amount
print(amount)
amount = str(amount)
print(amount)


# Payment
# A Payment Resource; create one using
# the above types and intent as 'sale'
payment = Payment({
    "intent": "sale",

    # Payer
    # A resource representing a Payer that funds a payment
    # Payment Method as 'paypal'
    "payer": {
        "payment_method": "paypal"},

    # Redirect URLs
    "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/"},

    # Transaction
    # A transaction defines the contract of a
    # payment - what is the payment for and who
    # is fulfilling it.
    "transactions": [{

        # ItemList
        "item_list": {
            "items": [{
                "name": "Donation",
                "sku": "item",
                "price": amount,
                "currency": "USD",
                "quantity": 1}]},

        # Amount
        # Let's you specify a payment amount.
        "amount": {
            "total": "5.00",
            "currency": "USD"},
        "description": "This is the payment transaction description."}]})

# Create Payment and return status
if payment.create():
    print("Payment[%s] created successfully" % (payment.id))
    # Redirect the user to given approval url
    for link in payment.links:
        if link.method == "REDIRECT":
            # Convert to str to avoid google appengine unicode issue
            # https://github.com/paypal/rest-api-sdk-python/pull/58
            redirect_url = str(link.href)
            print("Redirect for approval: %s" % (redirect_url))
else:
    print("Error while creating payment:")
    print(payment.error)