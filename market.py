'''
import urllib2
import datetime
date = datetime.date(2015,1,1).strftime("%s")
base_url = "https://api.gemini.com/v1"
response = urllib2.urlopen(base_url +
                            "/trades/btcusd?since=%s" % date)
print(response.read())
'''


import requests
'''
def data():
	response = requests.get('https://api.sandbox.gemini.com/v1' + '/btcusd',
                        headers=request_headers,
                        timeout=timeout,
                        verify=False)
	assert response.status_code == 200
	return response.content

x = data()
print(type(x))
'''

r = requests.get('https://api.sandbox.gemini.com/v1')
print(r.status_code)
data=r.json()