from subprocess import call
from subprocess import check_output
import json

merged = ""
count = 0

#Minimum hashrate in kH/s and minimum uptime 0-1
minHash = 1
minUptime = 0.5

#Gets wallet balance and takes away 0.1 to avoid fee issues.
#balance = check_output(["garlicoin-cli", "getbalance"])
#balance = balance.decode('utf-8')
balance = 50
balance -= 0.1

#Gets miner info from log.
with open('hashes.log','r') as inf:
    miners = eval(inf.read())

for item in miners:
    if 'uptime' in item:
        None
    elif 'count' in item:
        None
    else:
        count += 1

#Calculates how much each miner gets.
payout = str(float(balance) / count)

for item in miners:
    if 'uptime' in item:
        None
    elif 'count' in item:
        None
    else:
        miner = (float(miners[item]) / float(miners['count'])) * float(miners[item + 'uptime'])
        uptime = float(miners[item + 'uptime']) / float(miners['count'])
        if (miner > minHash and uptime > minUptime):
            print(uptime)
            merged = merged + '\\"' + item + '\\":' + payout + ','

merged = merged[:-1]
command = """sendmany "" "{""" + merged + '}"'
print(command)

#call(["garlicoin-cli", command])