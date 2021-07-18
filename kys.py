import requests
import json
import time

f = open("fuck.json") 
d = json.load(f)
lol = open("found.txt","a")

for i in d:
    url = f"https://api.everskies.com/user/check-alias"
    param = {"alias":i}
    time.sleep(0.5)
    r = requests.post(url,json=param)
    print(str(r.text + " : " + i))
    if r.text == "true":
      lol.write(i + "\n")
      lol.flush()
lol.close()
f.close()
