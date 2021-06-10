# -*- coding: utf-8 -*-
# This is a test job 
# It generates a list of random credentials and logs them into the data.log file
import string
import random
import datetime

credentials_length = 16
credentials_amount = 50
log_file = open("../../cron_logs/job1.log", "w")
log_file.write("Log date at: "+str(datetime.datetime.now())+"\n\n")

for y in range(credentials_amount):
    credential = ''.join(random.sample(string.ascii_uppercase + string.digits, k = credentials_length))
    log_file.write(credential+"\n")

log_file.close()
