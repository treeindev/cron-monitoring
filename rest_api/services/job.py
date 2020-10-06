from rest_api.database import Database
from rest_api.models.jobs import Job

class JobService():
    def __init__(self):
        self.database = Database()

    def get_all_jobs(self):
        self.database.connect()
        cursor = self.database.query("SELECT id, data, active, creation_date FROM jobs")
        jobs = [Job(*job) for job in cursor.fetchall()]
        self.database.close()
        return jobs
    
    def get_job(self, job_id):
        self.database.connect()
        cursor = self.database.query("SELECT id, data, active, creation_date from jobs WHERE id=%s", (job_id,))
        job = Job(*cursor.fetchone())
        self.database.close()
        return job
    
    def create_new_job(self, data, active):
        self.database.connect()
        cursor = self.database.query(
            "INSERT INTO jobs (data, active) VALUES (%s, %s) RETURNING id, data, active, creation_date",
            (data, 1 if active else 0)
        )
        job = Job(*cursor.fetchone())
        self.database.close()
        return job

    def update_job(self, job_id, data, active):
        self.database.connect()
        cursor = self.database.query(
            "UPDATE jobs SET data=%s, active=%s WHERE id=%s RETURNING id, data, active, creation_date",
            (data, 1 if active else 0, job_id)
        )
        job = Job(*cursor.fetchone())
        self.database.close()
        return job
    
    def remove_job(self, job_id):
        self.database.connect()
        self.database.query("DELETE FROM jobs WHERE id=%s", (job_id,))
        self.database.close()
        return True