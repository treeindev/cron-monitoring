from core.job_manager import JobManager
import json

manager = JobManager()

for job in manager.get_jobs():
    print(json.dumps(job.__dict__))