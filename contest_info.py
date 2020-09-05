import requests
import json
import datetime
import time


contest_url = 'https://codeforces.com/api/contest.list'
line_url = 'https://notify-api.line.me/api/notify'
num_future_contest = 10


def convert_time(timestamp : int) -> str:
    day = timestamp // (60 * 60 * 24)
    s1 = ' day ' if day == 1 else ' days '
    timestamp %= (60 * 60 * 24)
    hour = timestamp // (60 * 60)
    s2 = ' hour ' if hour == 1 else ' hours '
    timestamp %= (60 * 60)
    minute = timestamp // 60
    s3 = ' minute.' if minute == 1 else ' minutes.'

    return str(day) + s1 + str(hour) + s2 + str(minute) + s3


if __name__ == '__main__':
    r_json = requests.get(contest_url).json()
    messages = []

    for contest in r_json['result'][0:num_future_contest]:
        if (contest['phase'] == 'BEFORE'):
            start_unix_time = contest['startTimeSeconds']
            start_time = datetime.datetime.fromtimestamp(start_unix_time)
            time_before_start = -contest['relativeTimeSeconds']
            message = contest['name'] + ' start at ' + str(start_time) + ', in ' + convert_time(time_before_start)
            messages.append(message)

    messages.reverse()

    line_token = open('./token.txt', 'r').read()

    headers = {'Authorization': 'Bearer ' + line_token}

    payload = {'message': 'Comming contest'}
    res = requests.post(line_url, headers=headers, params=payload)

    for contest in messages:
        payload = {'message': contest}
        res = requests.post(line_url, headers=headers, params=payload)
        time.sleep(1)