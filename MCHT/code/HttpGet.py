import json
import time
import requests
import Constants as cst

def parseJson(text):
	res = json.load(text)
	print(res[0]['value'][0])

def HttpGetStatus():
	header = {'CK': 'DKFT0CB92XK9TPURA0'}
	r = requests.get('https://iot.cht.com.tw/iot/v1/device/19151157062/rawdata', headers = header)
	return r.json()[0]['value'][0]

def HttpGetPos():
	header = {'CK': 'DKUESE10ZAMYUZ4PMY'}
	r = requests.get('https://iot.cht.com.tw/iot/v1/device/19153468401/sensor/db_pos', headers = header)
	res = []
	for i in r.json()['attributes']:
		res.append(float(i['key']))
		res.append(float(i['value']))
	return res

def main():
	print(HttpGetPos())

if __name__ == '__main__':
	main()