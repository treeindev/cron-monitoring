from flask import Flask, jsonify, request

from .jobs import Job
from .database import Database

app = Flask(__name__)
database = Database()

@app.route('/jobs', methods=['GET'])
def get_jobs():
    database.connect()
    cursor = database.query("SELECT * FROM jobs")
    jobs = [Job(*job) for job in cursor.fetchall()]
    database.close()
    return jsonify({"jobs": [job.json() for job in jobs]})

@app.route('/job', methods=['POST'])
def new_job():
    # TODO: Implement a parser to ensure post data is received in the right format.
    data = request.get_json()
    database.connect()
    cursor = database.query(
        "INSERT INTO jobs (data, active) VALUES (%s, %s) RETURNING id, data, active, creation_date",
        (data['data'], 1 if data['active'] else 0)
    )
    job = Job(*cursor.fetchone())
    database.close()
    return jsonify(job.json())

@app.route('/job/<job_id>', methods=['GET'])
def get_job(job_id):
    database.connect()
    cursor = database.query("SELECT * from jobs WHERE id=%s", (job_id,))
    job = Job(*cursor.fetchone())
    database.close()
    return jsonify(job.json())

@app.route('/job/<job_id>', methods=['PUT'])
def update_job(job_id):
    return "Job updated"

@app.route('/job/<job_id>', methods=['DELETE'])
def delete_job(job_id):
    return "Job deleted"

@app.route('/<path>', methods=['GET','POST','PUT','DELETE','OPTIONS'])
def invalid_route(path):
    return jsonify({"error": "Invalid request"})