import requests
import sys
import argparse


user_info_url = 'https://codeforces.com/api/user.info'
line_url = "https://notify-api.line.me/api/notify"

parser = argparse.ArgumentParser()
parser.add_argument('user_name', help='user name you want to know about')
args = parser.parse_args()


if __name__ == '__main__':
    user_name = args.user_name
    payload = {'handles': user_name}
    result = requests.get(user_info_url, params=payload).json()

    if result['status'] == 'FAILED':
        print("User " + user_name + " not found.")
    else:
        diff = result['result'][0]['maxRating'] - result['result'][0]['rating']

    message = "Hello, " + user_name + ". Your current rating is " + str(result['result'][0]['rating']) \
        + ", " + str(diff) + " lower than highest."

    secret_token = open('./token.txt', 'r').read()

    headers = {"Authorization": "Bearer " + secret_token}
    line_payload = {"message": message}
    response = requests.post(line_url, headers=headers, params=line_payload)
