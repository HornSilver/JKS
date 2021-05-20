import requests

base_url = 'https://dft.huiliu.vip'
path_1 = '/account/getUsageRecord'
path_2 = '/account/getAccountInfo'
headers = {
	
	'token':'BmcDMQNgW2QEMg9tXzIIN1Y9WDlTLgc4BTBUZlFgAm4HewYzUzZQZQc1XTEMYAo3VjZSMQZmUmhUfwYy'
}
data = {

	"roomId": 0
}

fee_result = requests.request('POST',base_url+path_1,headers=headers,json=data)
account_result = requests.request('POST',base_url+path_2,headers=headers)

fee = fee_result.json()['data'][0]
acc = account_result.json()['data']

