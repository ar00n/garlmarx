import json
import urllib.request
from time import sleep

#Delay is the logging interval (in seconds)
delay = 10
log = {}

while True:
    url = 'http://garlmarx.fun/api/stats'
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    json2 = json.loads(r.decode('utf-8'))
    miners = json2["pools"]["garlicoin"]["workers"]

    for item in miners:
        try:
            old = log[item]
        except:
            old = 0
        if "MH" in miners[item]["hashrateString"]:
            hashRate = float(miners[item]["hashrateString"][:-3]) * 1000
            log[item] = (old + hashRate) / 2
        elif "KH" in miners[item]["hashrateString"]:
            hashRate = float(miners[item]["hashrateString"][:-3])
            log[item] = (old + hashRate) / 2

    file = open('hashes.log', 'w')
    file.write(str(log))
    file.close()
        
    print(log)
    sleep(delay)