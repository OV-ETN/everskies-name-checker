import requests
import json
import threading

names = json.load( open("fuck.json", "r") )
url = "https://api.everskies.com/user/check-alias"

goodNames = []

globalLock = threading.Lock()

def checkName(i):
    param = {"alias":i}
    r = requests.post(url,json=param)
    print(str(r.text + " : " + i))
    globalLock.acquire_lock()
    if r.text == "true":
      goodNames.append(i)
    globalLock.release_lock()

threadsAlive=[]

for i in names:
    thread=threading.Thread(target=checkName, args=(i,) )
    thread.start()
    threadsAlive.append(thread.is_alive)    

while True in [ Alive() for Alive in threadsAlive ]: pass
# wait for all threads to die

with open("found.txt","a") as out:
    for name in goodNames:
        out.write(name)
        out.write('\n')

print('Done')
