import requests
import hashlib
import hmac
import random
import string

api_url_preproduction = "https://preproduction.api.astrolinkbank.com"
api_key = "hrLFLjm.68iNHYUI4mVCWpsaAgwKPr0Rz-AD52JJqtLo."  # Replace with your API key
secret_key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))  # Replace with your real secret key

# Example data for the request (adjust as needed)
data = {
    "account_number": "123456789",
    "amount": 100.00,
    "currency": "GBP",
}

# Create HMAC signature using the secret_key
message = f"{api_url_preproduction}/transactions\n{str(data)}"
signature = hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()

# Set up request headers
headers = {
    "Api-Key": api_key,
    "Signature": signature,
}

# Make the GET request to the preproduction API
response = requests.get(f"{api_url_preproduction}/transactions", params=data, headers=headers)

# Print the response
print(response.status_code)
print(response.json())
