import requests

# NumVerify API access key
api_key = 'YOUR_API_KEY'

# Phone number to lookup
phone_number = 'PHONE_NUMBER_TO_LOOKUP'

# API endpoint
url = f'http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}'

try:
    # Send GET request to NumVerify API
    response = requests.get(url)
    data = response.json()

    # Extract relevant information from the response
    if data['valid']:
        country = data['country_name']
        location = data['location']
        carrier = data['carrier']
        line_type = data['line_type']

        # Print the reverse lookup information
        print(f"Phone Number: {phone_number}")
        print(f"Country: {country}")
        print(f"Location: {location}")
        print(f"Carrier: {carrier}")
        print(f"Line Type: {line_type}")
    else:
        print("Phone number not valid or information not found.")

except requests.RequestException as e:
    print(f"An error occurred: {e}")
