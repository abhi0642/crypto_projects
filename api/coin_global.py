import requests
import json

api_key='27a3cd16-58f5-48f6-81c1-127e3fde3fdd'

headers={'X-CMC_PRO_API_KEY':api_key}

base_url='https://pro-api.coinmarketcap.com'

global_url=base_url+'/v1/global-metrices/quotes/latest'


request=requests.get(global_url,headers=headers)
results=request.json()
print(json.dumps(results, sort_keys=True, indent=4))
