class Job:
    def __init__(self, _id, data, active, creation_date=''):
        self.identifier = _id
        self.data = data
        self.active = active
        self.creation_date = creation_date
    
    def is_job_active(self):
        return self.active == 1
    
    def json(self):
        return {
            "job_id": self.identifier,
            "data": self.data,
            "active": self.is_job_active(),
            "creation_date": self.creation_date 
        }