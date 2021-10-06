import subprocess
import tempfile
import os

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
            # Date and time section.
            time = details[0:5]

            # Script execution section.
            script = details[5].split(" && ", maxsplit=1)
            script_location = script[0].replace("cd ", "")
            script_execution = script[1].split(" >> ", maxsplit=1)

            # Output logs section.
            script_log = script_execution[1].split(" ", maxsplit=1)
            script_log_output = script_log[0]
            script_log_error = script_log[1]

            jobs.append(
                Job(
                    time[0],
                    time[1],
                    time[2],
                    time[3],
                    time[4],
                    script_location,
                    script_execution[0],
                    script_log_output,
                    script_log_error
                )
            )

        return jobs

    # Add a crontab job to the system.
    # The creation of new crontab jobs is done via temporary file.
    # All current jobs + new added one are written on a temporary TXT file.
    # Then, crontab commmand gets executed based on the temporary file.
    # After crontab gets update, temporary file is manually removed.
    # To manage temp files, "NamedTemporaryFile" is used from the tempfile module. See: https://docs.python.org/3/library/tempfile.html
    def add_job(self, minutes, hours, days, month, week_day, location, execution, output, error) -> Job:
        new_job = Job(minutes, hours, days, month, week_day, location, execution, output, error)
        jobs = self.get_jobs()
        jobs.append(new_job)

        # TODO: Prevent adding a duplicated job

        # Generate a temporary named file.
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')

        # Loop through all jobs and add new line to temporary file.
        for job in jobs:
            tmp_file.write(bytes(self.__create_crontab(job)+"\n", encoding="utf-8"))
        tmp_file.close()
        
        # Remove all jobs + re-add new ones.
        self.__remove_all()
        subprocess.run([self.crontab_base, tmp_file.name])

        # Clean up temporary file.
        os.unlink(tmp_file.name)
    
    # Removes all crontab jobs from the system.
    # CAUTION: There is no rollback once the command gets executed.
    def __remove_all(self) -> None:
        subprocess.run([self.crontab_base, self.crontab_remove])

    # Creates a crontab string based on a given job
    def __create_crontab(self, job) -> str:
        # Date and time section.
        crontab = f"{job.minutes} {job.hours} {job.days} {job.month} {job.week_day} "
        # Script execution section.
        crontab += f"cd {job.location} && {job.execution} "
        # Output logs section.
        crontab += f">> {job.output} {job.error}"
        return crontab
