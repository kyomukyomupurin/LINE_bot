import requests
import json
import datetime
import time


url = 'https://codeforces.com/api/contest.list'
r = requests.get(url)
r_json = r.json()
num_future_contest = 10

messages = []

for info in r_json['result'][0:num_future_contest]:
    if (info["phase"] == "BEFORE"):
        start_unix_time = info["startTimeSeconds"]
        start_time = datetime.datetime.fromtimestamp(start_unix_time)
        time_before_start = -info["relativeTimeSeconds"]
        day_before_start = time_before_start // (60 * 60 * 24)
        time_before_start %= (60 * 60 * 24)
        hour_before_start = time_before_start // (60 * 60)
        time_before_start %= (60 * 60)
        minutes_before_start = time_before_start // 60
        message = info["name"] + " start at " + \
            str(start_time) + ", in " + \
            str(day_before_start) + " days " + \
            str(hour_before_start) + " hours " + \
            str(minutes_before_start) + " minutes."
        messages.append(message)

messages.reverse()

secret_token = ""

with open('./token.txt', 'r') as f:
    secret_token = f.read()

line_url = "https://notify-api.line.me/api/notify"
token = secret_token
headers = {"Authorization": "Bearer " + token}

for contest in messages:
    payload = {"message": message}
    res = requests.post(line_url, headers=headers, params=payload)
    time.sleep(3)
