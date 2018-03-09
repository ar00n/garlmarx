import json
import urllib.request
from time import sleep
from ast import literal_eval

#Delay is the logging interval (in seconds)
delay = 10
count = 0
log = {}
log['count'] = '0'

try:
    f = open('hashes.log', 'r')
    log = literal_eval(f.read())
except:
    print('No log found.')

while True:
    url = 'http://garlmarx.fun/api/stats'
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    json2 = json.loads(r.decode('utf-8'))
    miners = json2["pools"]["garlicoin"]["workers"]
    log['count'] = str(int(log['count']) + 1)

    for item in miners:
        try:
            old = log[item]
            uptime = log[item + 'uptime']
        except:
            old = 0
            uptime = 0
        if "MH" in miners[item]["hashrateString"]:
            hashRate = float(miners[item]["hashrateString"][:-3]) * 1000
            log[item] = (old + hashRate) / 2
            log[item + 'uptime'] = str(int(uptime) + 1)
        elif "KH" in miners[item]["hashrateString"]:
            hashRate = float(miners[item]["hashrateString"][:-3])
            log[item] = (old + hashRate) / 2
            log[item + 'uptime'] = str(int(uptime) + 1)
            
    file = open('hashes.log', 'w')
    file.write(str(log))
    file.close()
        
    print(log)
    sleep(delay)