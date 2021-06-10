import os
import subprocess

output = subprocess.run(['crontab', '-l'], stdout=subprocess.PIPE)
list = output.stdout.decode('utf-8').splitlines();
print(len(list))