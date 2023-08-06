import requests
import json


def make_header(token):
    return {
        "Authorization": f'Zoho-oauthtoken {token.access}'
    }

def get_users(token, **kwargs):
    url = "https://www.zohoapis.com/crm/v2.1/users"

    headers = make_header(token)

    response = requests.get(url=url, headers=headers, params=kwargs)

    if response.status_code == 401:
        token.generate()
        return get_users(token, **kwargs)

    else:
        content = json.loads(response.content.decode('utf-8'))
        return token, content.get("users")


def add_user(token, user_object):
    url = 'https://www.zohoapis.com/crm/v2.1/users'

    headers = make_header(token)

    request_body = {}
    user_list = [user_object]

    request_body['users'] = user_list

    data = json.dumps(request_body).encode('utf-8')

    response = requests.post(url=url, headers=headers,data=data)

    if response.status_code == 401:
        token.generate()
        return add_user(token, user_object)

    else:
        return token, response.status_code, json.loads(response.content.decode('utf-8'))


