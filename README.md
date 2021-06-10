# Cron Monitoring

Cron Monitoring is a tool to manage Cron Jobs running on a local machine. It allows to keep track of active jobs, add new jobs or remove existing ones.

Cron Jobs allow you to run scheduled scripts at a given date and time. They are very helpful to execture routines periodically. Backups, data cleanup, send daily reports, check server availability or health checks are examples of Cron Jobs usecases.

## Cron Jobs Syntax

This tool manages the creation of Cron Job behind scenes. However, here is the details of how these jobs look like. A typical Cron Job has the following syntax:

```bash
1 2 3 4 5 /path/to/script arg1 arg2
```

Where:
* `1` refers to Minute (0-59).
* `2` refers to Hours (0-23).
* `3` refers to Day (0-31).
* `4` refers to Month (0-12) - `12` being December.
* `5` refers to Day of Week (0-7) - `0` or `7` being Sunday.
* `path/to/script` refers to location of your script.

Here is the table for reference:
```bash
* * * * * script to be executed
- - - - -
| | | | |
| | | | ----- Day of week (0 - 7) (Sunday=0 or 7)
| | | ------- Month (1 - 12)
| | --------- Day of month (1 - 31)
| ----------- Hour (0 - 23)
------------- Minute (0 - 59)
```

For system jobs, a Cron Job also adds the `USERNAME` of the user that will run the job.

```bash
1 2 3 4 5 USERNAME /path/to/script arg1 arg2
```

By default the output of a command or a script (if any produced), will be email to your local email account. To stop receiving email output from crontab you need to append `>/dev/null 2>&1`. Example:
```bash
* * * * * /root/script.sh >/dev/null 2>&1
```

### Cron Jobs Examples
Run a job everyday at 3am:
```bash
0 3 * * * /root/job.sh
```

Run a job 5 minutes after midnight everyday:
```bash
5 0 * * * /root/job.sh
```

Run a python script first day of every month:
```bash
0 0 1 * * /root/job.sh
```

### Crontab
More info about Crontab: https://man7.org/linux/man-pages/man1/crontab.1.html