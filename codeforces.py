import requests
import sys


user_info_url = 'https://codeforces.com/api/user.info'
line_url = "https://notify-api.line.me/api/notify"


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Enter a user name!")
        exit(0)

    user_name = sys.argv[1]
    payload = {'handles': user_name}
    result = requests.get(user_info_url, params=payload).json()

    if result['status'] == 'FAILED':
        print("User " + user_name + " not found.")
    else:
        diff = result['result'][0]['maxRating'] - result['result'][0]['rating']

    message = "Hello, " + user_name + ". Your current rating is " + str(result['result'][0]['rating']) \
        + ", " + str(diff) + " lower than highest."

    secret_token = ""

    with open('./token.txt', 'r') as f:
        secret_token = f.read()

    headers = {"Authorization": "Bearer " + secret_token}
    line_payload = {"message": message}
    response = requests.post(line_url, headers=headers, params=line_payload)
