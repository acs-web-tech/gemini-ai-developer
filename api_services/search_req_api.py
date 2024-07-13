import requests

api_key = "my_api_key"

url = "http://4dcloud.cloud/apis/search_vector"

headers = {
    "4dcloud-auth-token": api_key,
    "Content-Type": "application/json"
}

body = {
    "projectid":"34554544",
    "query":"father son",
    "result_count":5                                                                                                                                                                                                                                                                
}

response = requests.post(url, headers=headers,  json=body)
if response.status_code == 200:
    print("search results", response.json())
else:
    print("response failed", response.status_code, response.text)