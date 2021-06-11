import subprocess
import json

output = subprocess.run(['crontab', '-l'], stdout=subprocess.PIPE)
crons = output.stdout.decode('utf-8').splitlines();
jobs = []

for cron in crons:
    details = cron.split(" ", maxsplit=5)
    time = details[0:5]
    script = details[5].split(" && ", maxsplit=1)
    script_location = script[0].replace("cd ", "")
    script_execution = script[1].split(" >> ", maxsplit=1)

    # TODO: Script data log should be better formatted. 

    jobs.append({
        "minutes": time[0],
        "hours": time[1],
        "day": time[2],
        "month": time[3],
        "week_day": time[4],
        "script_location": script_location,
        "script_execution": script_execution[0],
        "script_log": script_execution[1]
    })
print(json.dumps(jobs))