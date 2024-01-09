import requests
import urllib.parse as urlparse
import json
import pyperclip as ps
import webbrowser as wb
import sys

cobalt = "https://co.wuk.sh/api/json"
url = ps.paste()
encoded_url = urlparse.quote(url)
headers = {
    "Accept":"application/json",
    "Content-Type":"application/json",
    }
data = {
"url":encoded_url
}
data = json.dumps(data)


try: 
    response = requests.post(cobalt, headers=headers, data=data)

    if response.status_code == 200:
        print(response.json()['url'])
        print("Success")
    else:
        print("Failed")
        print(response.json())

except Exception as e:
    print(e)

def open_url(url):
    wb.open(url)

open_url(response.json()['url'])

sys.exit()



