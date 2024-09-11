import os
import ipinfo
import subprocess as sb
from colorama import init, Fore

try:
	import requests
except:
	os.system('pip install requests')
	import requests

try:
	from bs4 import BeautifulSoup as bs4
except:
	os.system('pip install bs4')
	from bs4 import BeautifulSoup as bs4

def clear_console():
	try:
		os.system('cls')
	except:
		sb.call('clear')


print(Fore.GREEN + """
		_ _  _ _ _
		 |  |     |
		 |  |_ _ _|
		 |  |
		_|_ |
		_ _         _ _ _  _ _ _
		 |  |\   | |      |     |
		 |  | \  | |_ _   |     |
		 |  |  \ | |      |     |
		_|_ |   \| |      |_ _ _|
		
		""")


ip = input(Fore.CYAN + "Please enter an IP address: ")
access_token = "cda874226c0c24"

try:
	handler = ipinfo.getHandler(access_token)
	details = handler.getDetails(ip)
except:
	print(Fore.RED + "Sorry, big error, please try again it!")


try:
	print(Fore.GREEN + f"""
		MAIN INFO

		|IP | {details.ip} |
		| HOSTNAME | {details.hostname} |
		| CITY | {details.city} |
		| REGION | {details.region} |
		| COUNTRY | {details.country} |
		| LOC | {details.loc} |
		| ORG | {details.org} |
		| TIMEZONE | {details.timezone} |
		""")
except:
	print(Fore.RED + "Error! Try it again!")



def on_request_uri():
	url = 'https://ip2geolocation.com/?ip=' + str(ip)
	print('>>> link on ipinfo >>>' + str(url))

on_request_uri()