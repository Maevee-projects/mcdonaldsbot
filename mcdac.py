import requests
import sys
import random
import urllib3
import datetime
import time
import json
import string
import pyqrcode
import png
import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.WHITE)
print(Style.BRIGHT)
print('Создатель:\nhttps://lolz.guru/maevee/\nhttps://bhf.biz/members/174108/')
print(Style.RESET_ALL)
print(Style.BRIGHT)
print(Fore.BLUE)
print('Создатель:\nhttps://lolz.guru/maevee/\nhttps://bhf.biz/members/174108/')
print(Style.RESET_ALL)
print(Style.BRIGHT)
print(Fore.RED)
print('Создатель:\nhttps://lolz.guru/maevee/\nhttps://bhf.biz/members/174108/')
print(Style.RESET_ALL)
print(Fore.GREEN)
apikey = input('Введите ваш api ключ сервиса sms-activate:')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def macdac():
	a = int(input('сколько бигов хочешь?\n'))
	while a > 0:
		url2 = f"https://sms-activate.ru/stubs/handler_api.php?api_key={apikey}&action=getNumber&service=ry&country=0"
		url1 = 'https://mobile-api.mcdonalds.ru/api/v1/user/login/phone'
		KEY_LEN = 16
		def base_str():
		    return (string.hexdigits)
		oppp = random.choices(base_str(), k=KEY_LEN)
		deviceid = (''.join(oppp))
		headers = {'X-Device-ID': deviceid, 'user-agent': 'okhttp/3.12.1'}
		r2 = requests.post(url2, verify=False)
		time.sleep(5)
		response_r2 = r2.text
		if response_r2 == 'NO_NUMBERS':
			print('че с номерами(их нет)')
			time.sleep(100)
			print('сплю 100 секунд и ищу еще раз номер')
			mcdac()
		if response_r2 == 'NO_BALANCE':
			sys.exit('че с деньгами(их нет)')
		else:
			ACCESS_NUMBER = r2.text
			start_number = ACCESS_NUMBER.find(':7')
			null = ACCESS_NUMBER[14:start_number]
			aaa = start_number + 1
			number = ACCESS_NUMBER[aaa:36]
		time.sleep(5)
		numberres = "+" + number
		url3 = f'https://sms-activate.ru/stubs/handler_api.php?api_key={apikey}&action=setStatus&status=1&id={null}'
		r1 = requests.post(url1, verify=False, headers=headers, json={"phone": numberres})
		res = json.loads(r1.text)
		JWTONLOGIN = res['ticket']
		time.sleep(5)
		r3 = requests.post(url3, verify=False)
		time.sleep(100)
		url4 = f'https://sms-activate.ru/stubs/handler_api.php?api_key={apikey}&action=getStatus&id={null}'
		r4 = requests.post(url4, verify=False)
		str = 'STATUS_OK'
		for s in r4.text:
		    if str.lower().find(s.lower()) != -1:
		        s = 'True'
		        break
		if s == 'True':
			CODE = r4.text[10:15]
		if r4.text == 'STATUS_WAIT_CODE':
			print('че с смской(её нет, timeout), продолжаю выполнение')
			macdac()
		if r4.text == 'NO_ACTIVATION':
			sys.exit('че то не то')
		url5 = 'https://mobile-api.mcdonalds.ru/api/v1/user/login/phone/confirm'
		r5 = requests.post(url5, verify=False, headers=headers, json={"code": CODE, "ticket": JWTONLOGIN})
		res2 = json.loads(r5.text)
		token = res2['token']
		headersonlog = {'X-Device-ID': deviceid, 'user-agent': 'okhttp/3.12.1', 'authorization': "Bearer " + token}
		url7 = 'https://mobile-api.mcdonalds.ru/api/v1/awards'
		r7 = requests.get(url7, verify=False, headers=headersonlog)
		while r7.text == "[]":
			time.sleep(5)
			r7 = requests.get(url7, verify=False, headers=headersonlog)
		res5 = json.loads(r7.text)
		idaward = res5[0]['id']
		url6 = f'https://mobile-api.mcdonalds.ru/api/v1/offers/offer/{idaward}'
		r6 = requests.get(url6, verify=False, headers=headersonlog)
		res3 = json.loads(r6.text)
		isActive = res3['isActive']
		time.sleep(10)
		if isActive == "false":
			sys.exit('че с акцией(её нет)')
		print('Выполнение завершено. Записываю код в файл.')
		open('bigmacs.txt', 'w')
		f = open('bigmacs.txt','a')
		mcdcode = "https://tavernamobot.pw/nnac.php?q=" + token + "\n"
		f.write(mcdcode)
		f.close()
		a = a - 1
macdac()
