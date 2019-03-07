import requests
from getpass import getpass
import json


identifier = 'kreshel'
secret = getpass('Enter password: ')
'''
r1 = requests.get(url='https://api.github.com/user')
print('Without auth: ', r1.status_code)

r2 = requests.get(url='https://api.github.com/user', auth=(identifier,secret))
print('With auth: ', r2.status_code)


print()
if r1.status_code == 200:
	print(r1.content)

if r2.status_code == 200:
	print(r2.json())
'''

r3 = requests.get(url='https://api.tacc.utexas.edu/clients/v2', auth=(identifier,secret))
r4 = requests.post(url='https://api.tacc.utexas.edu/clients/v2', auth=(identifier,secret), data={"clientName":"this_name"})
consumerKey = 
#r5 = requests.post()
#print(json.dumps(r3.json(), indent=3))