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


# courses
def create_event(token, event_args):
    eventbrite = Eventbrite(token)
    try:
        event = eventbrite.post_event(event_args)
    except Exception:
        print(Exception)

    return event


def update_event(token, event_id, event_args):
    eventbrite = Eventbrite(token)
    event = eventbrite.post("/events/{}/".format(event_id), data=event_args)
    return event


def delete_event(token, event_id):
    eventbrite = Eventbrite(token)
    event = eventbrite.delete("/events/{}/".format(event_id))
    return event

def publish_event(token, event_id):
    eventbrite = Eventbrite(token)
    event = eventbrite.publish_event(event_id)
    return event
