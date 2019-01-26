import requests
import json
from eventbrite import Eventbrite


def get_oauth_token(code):
    url = "https://www.eventbrite.com/oauth/token"
    payload = {
        "code": code,
        "client_secret": "J46K2BZ5VOMAE7EAFV5VNMRUIOLGRAMCAV5EQKNE37FDR4ZSBM",
        "client_id": "ITIJ3MIIJL62GAFV5D",
        "grant_type": "authorization_code",
    }
    headers = {"content-type": "application/x-www-form-urlencoded"}
    response = requests.post(url=url, data=payload, headers=headers)
    json_data = json.loads(response.text)
    print(json_data)
    return json_data["access_token"]


def get_user(token):
    eventbrite = Eventbrite(token)
    user = eventbrite.get_user()
    return user


def get_user_orders(token):
    eventbrite = Eventbrite(token)
    orders = eventbrite.get_user_orders()
    return orders
