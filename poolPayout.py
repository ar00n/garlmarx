from subprocess import call
from subprocess import check_output
import json

#Minimum hashrate for payouts
minHash = 100

#Gets wallet balance.
balance = check_output(["garlicoin-cli", "getbalance"])
balance = balance.decode('utf-8')
#balance = 50

#Gets miner info from log.
with open('hashes.log','r') as inf:
    miners = eval(inf.read())

#Calculates how much each miner gets.
payout = str(float(balance) / len(miners))
merged = ""

for item in miners:
    if miners[item] > minHash:
        merged = merged + '\\"' + item + '\\":' + payout + ','

merged = merged[:-1]
command = """sendmany "" "{""" + merged + '}"'

call(["garlicoin-cli", command])