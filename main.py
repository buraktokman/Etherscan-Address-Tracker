#!/usr/bin/env python3
# coding=utf-8
'''
#-------------------------------------------------------------------------------
Project		: Etherscan Address Tracker
Module		: main
Purpose   	: Notify me when a new trade has been reported
Version		: 0.0.1 alpha
Status 		: Development

Modified	: 2021 Mar 5
Created   	: 2021 Mar 5
Author		: Burak Tokman
Email 		: buraktokman@hotmail.com
Copyright 	: 2021, Bulrosa OU
Licence   	: EULA
			  Unauthorized copying of this file, via any medium is strictly prohibited
			  Proprietary and confidential
#-------------------------------------------------------------------------------
'''

from etherscan import Etherscan
import time

CONFIG = {'api_key': '',
			'address': ''}

'''
https://github.com/pcko1/etherscan-python

'''

def main():
	global CONFIG

	print('Connecting to Etherscan')
	try:
		eth = Etherscan(CONFIG['api_key'])
		print('Connected!')
	except Exception as e:
		print('ERROR: Can\'t Connect')
		raise e


	start_balance = eth.get_eth_balance(address=CONFIG['address'])
	print(f'Balance: {start_balance}')
	print('Watching transactions...')

	# CHECK BALANCE
	while True:

		current_balance = eth.get_eth_balance(address=CONFIG['address'])

		# NOTIFY IF CHANGE DETECTED
		if start_balance != current_balance:
			print('Transaction made!')
			print(f'New Balance: {start_balance}')

			#
			#	INCOMPLETE - TX DETAILS HERE
			#
		else:
			pass
			# print('Nothing new...')

		start_balance = current_balance

		# Wait
		time.sleep(1)


if __name__ == '__main__':
	main()