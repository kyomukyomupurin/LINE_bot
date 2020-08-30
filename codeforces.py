import requests


payload = {'handles': 'kyomukyomupurin'}
r = requests.get('https://codeforces.com/api/user.info', params=payload)
diff = r.json()['result'][0]['maxRating'] - r.json()['result'][0]['rating']
message = "Hello! " + payload['handles'] + ". Your current rating is " + str(diff) + " less than highest."

secret_token = ""

with open('./token.txt', 'r') as f:
    secret_token = f.read()

url = "https://notify-api.line.me/api/notify"
token = secret_token
headers = {"Authorization": "Bearer " + token}
payload = {"message": message}
res = requests.post(url, headers=headers, params=payload)
