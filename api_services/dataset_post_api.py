import requests
import json

api_key = "my_api_key"

url = "http://4dcloud.cloud/apis/insertvector_json"

headers = {
    "4dcloud-auth-token": api_key,
    "Content-Type": "application/json"
}

body = [{
yourkey:value,

}]

response = requests.post(url, headers=headers,  body = json.dumps(body))
if response.status_code == 200:
    print("search results", response.json())
else:
    print("response failed", response.status_code, response.text)