import requests

res = requests.get('https://scotch.io')

print(res.status_code)
if res:
    print('Response OK')
else:
    print('Response Failed')

print(res.headers)
