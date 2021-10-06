# -*- coding: utf-8 -*-
# This is a test job 
# It logs the current date to a log file
import datetime

credentials_length = 16
credentials_amount = 50
log_file = open("../../cron_logs/job3.log", "w")
log_file.write("I have run at: "+str(datetime.datetime.now())+"\n\n")
log_file.close()
