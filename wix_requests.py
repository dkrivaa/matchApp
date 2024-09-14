import requests
import json


def generic_request(url, data):
    # Headers to specify the request format (JSON)
    headers = {
        'Content-Type': 'application/json'
    }
    # Sending the POST request
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        # Check if the request was successful
        if response.status_code == 200:
            print("Success! Data received:", response.json())
        else:
            print(f"Failed with status code: {response.status_code}, Error: {response.text}")
    except Exception as e:
        print(f"Error sending request: {e}")


def reading_request():
    url = 'https://dannykrivaa.wixsite.com/matchapp/_functions/messages'
    data = {
        'message': 'Getting files ready....'
    }
    generic_request(url, data)


def tests_request(message):
    url = 'https://dannykrivaa.wixsite.com/matchapp/_functions/messages'
    data = {
        'message': f'{message}. Please correct the problem and upload again.'
    }
    generic_request(url, data)

def start_match_request():
    url = 'https://dannykrivaa.wixsite.com/matchapp/_functions/messages'
    data = {
        'message': 'Files checked. Continuing process....'
    }
    generic_request(url, data)

def finish_match_request():
    url = 'https://dannykrivaa.wixsite.com/matchapp/_functions/messages'
    data = {
        'message': 'Finishing process, getting results....'
    }
    generic_request(url, data)


