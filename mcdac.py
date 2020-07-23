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
import datetime
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
a = int(input('сколько бигов хочешь?\n'))
def macdac():
			global a
			url2 = f"https://sms-activate.ru/stubs/handler_api.php?api_key={apikey}&action=getNumber&service=ry&country=0"
			url1 = 'https://mobile-api.mcdonalds.ru/api/v1/user/login/phone'
			KEY_LEN = 16
			https_proxy = "socks5://127.0.0.1:8883"
			httpbin = 'http://httpbin.org/get'
			proxyDict = { 
		             "http" : https_proxy,
		             "https" : https_proxy
					}
			def base_str():
			    return (string.hexdigits)
			oppp = random.choices(base_str(), k=KEY_LEN)
			deviceid = (''.join(oppp))
			deviceid = deviceid.lower()
			headers = {'X-Device-ID': deviceid, 'X-Device-Model': 'google Pixel 2', 'X-Platform': 'Android', 'X-OS-Version': '22', 'X-Language': 'ru_RU', 'X-App-Version': '7.2.1', 'X-Build-Number': '2524', 'X-Cellular-Name': 'Mobile TeleSystems', 'X-City-ID': '5dfc9fef51f0dc92455befe5', 'X-Timezone': 'GMT+03:00', 'user-agent': 'okhttp/3.12.1'}
			r2 = requests.post(url2, verify=False)
			time.sleep(5)
			response_r2 = r2.text
			if response_r2 == 'NO_NUMBERS':
				print('че с номерами(их нет)')
				print('сплю 100 секунд и ищу еще раз номер')
				time.sleep(100)
				macdac()
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
			print('Сплю 30 секунд, чтобы не получить блокировку в маке')
			time.sleep(30)
			r1 = requests.post(url1, verify=False, headers=headers, proxies=proxyDict, json={"phone": numberres})
			if r1.status_code == 429:
				print('Слишком много запросов, нужно подождать 10 минут и снова запустить программу')
				sys.exit()
			print('Номер успешно получен! Вбиваю номер в мак.')
			res = json.loads(r1.text)
			JWTONLOGIN = res['ticket']
			time.sleep(5)
			r3 = requests.post(url3, verify=False, proxies=proxyDict)
			print('Сплю 100 секунд и проверяю номер на наличие смс')
			time.sleep(100)
			url4 = f'https://sms-activate.ru/stubs/handler_api.php?api_key={apikey}&action=getStatus&id={null}'
			r4 = requests.post(url4, verify=False, proxies=proxyDict)
			str = 'STATUS_OK'
			for s in r4.text:
			    if str.lower().find(s.lower()) != -1:
			        s = 'True'
			        break
			if s == 'True':
				CODE = r4.text[10:15]
			if r4.text == 'STATUS_WAIT_CODE':
				print('че с смской(её нет, timeout), продолжаю выполнение')
				urlcancel = f"https://sms-activate.ru/stubs/handler_api.php?api_key={apikey}&action=setStatus&status=8&id={null}"
				rcancel = requests.post(urlcancel, verify=False, proxies=proxyDict)
				macdac()
			if r4.text == 'NO_ACTIVATION':
				sys.exit('че то не то, напишите создателю')
			print('Нашел смс! Подтверждаю номер в маке.')
			url5 = 'https://mobile-api.mcdonalds.ru/api/v1/user/login/phone/confirm'
			r5 = requests.post(url5, verify=False, headers=headers, proxies=proxyDict, json={"code": CODE, "ticket": JWTONLOGIN})
			res2 = json.loads(r5.text)
			token = res2['token']
			headersonlog = {'X-Device-ID': deviceid, 'user-agent': 'okhttp/3.12.1', 'authorization': "Bearer " + token}
			url7 = 'https://mobile-api.mcdonalds.ru/api/v1/awards'
			r7 = requests.get(url7, verify=False, proxies=proxyDict, headers=headersonlog)
			while r7.text == "[]":
				time.sleep(5)
				r7 = requests.get(url7, verify=False, proxies=proxyDict, headers=headersonlog)
			res5 = json.loads(r7.text)
			idaward = res5[0]['id']
			url6 = f'https://mobile-api.mcdonalds.ru/api/v1/offers/offer/{idaward}'
			print('Получаю бигмак')
			r6 = requests.get(url6, verify=False, proxies=proxyDict, headers=headersonlog)
			res3 = json.loads(r6.text)
			isActive = res3['isActive']
			availabilityTime = res3['availabilityTime']
			value = datetime.datetime.fromtimestamp(availabilityTime)
			time.sleep(10)
			if isActive == "false":
				sys.exit('че с акцией(её нет)')
			print('Выполнение завершено. Записываю код в файл.')
			f = open('bigmacs.txt','a')
			mcdcode = "\n" + "http://r906914q.beget.tech/new.php?jwt=" + token + "\n"
			f.write(mcdcode + "" + "////////" + value.strftime('%Y-%m-%d %H:%M:%S') + "- В это время код перестанет обновляться(7дней)")
			a = a - 1
while a > 0:
			macdac()
