from twilio.rest import Client
# make sure you have twillio installed as a python library "pip install twilio"
#
# Your Twilio account SID and auth token
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'

# Twilio phone number and recipient's phone number
twilio_number = 'YOUR_TWILIO_PHONE_NUMBER'
recipient_number = 'RECIPIENT_PHONE_NUMBER'

# Create the Twilio client
client = Client(account_sid, auth_token)

# Compose the message
message = "Hello! This is a test message."

try:
    # Send the message
    client.messages.create(
        body=message,
        from_=twilio_number,
        to=recipient_number
    )
    print("Message sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
