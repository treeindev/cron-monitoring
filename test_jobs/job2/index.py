import requests
import json
import datetime

my_cryptos = {"bitcoin", "ethereum", "cardano", "litecoin"}
log_file = open("../../cron_logs/job2.log", "a")
log_file.write("Crypto Price at: "+str(datetime.datetime.now())+"\n\n")

response = requests.get("https://api.coincap.io/v2/assets")
cryptos = json.loads(response.text)
for crypto in cryptos["data"]:
    if crypto["id"] in my_cryptos:
        log_file.write(crypto["id"]+" - "+crypto["priceUsd"]+"$\n")

log_file.write("\n================================\n\n\n\n")
log_file.close()