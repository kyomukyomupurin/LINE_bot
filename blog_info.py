import requests
import json
import datetime
import time


blog_url = 'https://codeforces.com/blog/entry/'
blog_api_url = 'https://codeforces.com/api/blogEntry.view'
line_url = 'https://notify-api.line.me/api/notify'
max_post_day = 50


def search_nextId():
    payload['blogEntryId'] = str(int(payload['blogEntryId']) + 1)
    r_json = requests.get(blog_api_url, params=payload).json()
    time.sleep(0.5)

    if r_json['status'] == 'OK':
        last_blogEntryId = payload['blogEntryId']
        blog_urls.append(blog_url + last_blogEntryId)

        with open('./last_blogEntryId.txt', 'w') as f:
            f.write(last_blogEntryId)


if __name__ == '__main__':
    last_blogEntryId = ""

    with open('./last_blogEntryId.txt', 'r') as f:
        last_blogEntryId = f.read()

    payload = {'blogEntryId' : last_blogEntryId}

    blog_urls = []

    for i in range(max_post_day):
        search_nextId()

    line_token = ''

    with open('./token.txt', 'r') as f:
        line_token = f.read()

    headers = {'Authorization': 'Bearer ' + line_token}
    payload = {'message': 'New blog posts'}
    res = requests.post(line_url, headers=headers, params=payload)

    for url in blog_urls:
        blog_payload = {'message': url}
        res = requests.post(line_url, headers=headers, params=blog_payload)
        time.sleep(1)
