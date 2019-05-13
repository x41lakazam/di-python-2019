from PyLinkedinAPI.PyLinkedinAPI import PyLinkedinAPI
import requests
import json

# Get the token
client_id = "86guba3qr0tw12"
client_secret = "ALUW4danYPTvjpBe"
auth_url = r"https://www.linkedin.com/oauth/v2/authorization"

req = requests.get(auth_url)
print(req.json())


instance = PyLinkedinAPI(access_token)
profile = instance.get_basic_profile()
print(profile)
