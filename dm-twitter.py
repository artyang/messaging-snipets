import tweepy

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create the API object
api = tweepy.API(auth)

# Send a DM
recipient_id = 'RECIPIENT_USER_ID'
message = 'Hello! This is a direct message.'

try:
    api.send_direct_message(recipient_id, message)
    print("Direct message sent successfully!")
except tweepy.TweepError as e:
    print(f"An error occurred: {e}")
