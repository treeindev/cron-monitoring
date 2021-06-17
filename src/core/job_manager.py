import subprocess

from .job import Job

class JobManager:
    crontab_base = "crontab"
    crontab_list = "-l"
    crontab_remove = "-r"
    crontab_file = "../samples.txt"

    # Returns list of running jobs on the system
    def get_jobs(self) -> list:
        output = subprocess.run([self.crontab_base, self.crontab_list], stdout=subprocess.PIPE)
        crons = output.stdout.decode('utf-8').splitlines();
        jobs = []

        # TODO: Check for "no crontab for" values if no jobs are running on the system.

        for cron in crons:
            details = cron.split(" ", maxsplit=5)
            time = details[0:5]
            script = details[5].split(" && ", maxsplit=1)
            script_location = script[0].replace("cd ", "")
            script_execution = script[1].split(" >> ", maxsplit=1)
            script_log = script_execution[1].split(" ", maxsplit=1)
            script_log_output = script_log[0]
            script_log_error = script_log[1]

            jobs.append(
                Job(time[0], time[1], time[2], time[3], time[4], script_location, script_execution[0], script_log_output, script_log_error)
            )

        return jobs

    def add_job(self, minutes, hours, days, month, week_day, location, execution, output, error) -> Job:
        new_job = Job(minutes, hours, days, month, week_day, location, execution, output, error)
        jobs = self.get_jobs()
        jobs.append(new_job)

        # TODO: Use tempdir module to manage temporary files.
        # https://docs.python.org/3/library/tempfile.html

        # Generate a temporary file.
        # Loop through all jobs and add new line to temporary file.
        # Remove all jobs from crontab.
        # Execute crontab command to add jobs from temporary file.
        # Clean up temporary file.

    
    def remove_all(self) -> None:
        subprocess.run([self.crontab_base, self.crontab_remove])
    
    def add_jobs(self) -> None:
        subprocess.run([self.crontab_base, self.crontab_file])
