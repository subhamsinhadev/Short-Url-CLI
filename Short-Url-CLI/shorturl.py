import requests
import sys
if len(sys.argv)>1:
    text=sys.argv[1]
else:
    print("use format url.py link")
    
datas={"url":text}
response=requests.post(url="https://cleanuri.com/api/v1/shorten"
                       ,json=datas)
if response.status_code==200:
    result=response.json()
    print("Short Url:",result.get('result_url'))

