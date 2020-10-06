from flask import Blueprint, jsonify, request
from rest_api.services.job import JobService

api = Blueprint('api', __name__)
job_service = JobService()

@api.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = job_service.get_all_jobs()
    return jsonify({"jobs": [job.json() for job in jobs]})

@api.route('/job', methods=['POST'])
def new_job():
    # TODO: Implement a parser to ensure post data is received in the right format.
    data = request.get_json()
    job = job_service.create_new_job(data['data'], data['active'])
    return jsonify(job.json())

@api.route('/job/<job_id>', methods=['GET'])
def get_job(job_id):
    job = job_service.get_job(job_id)
    return jsonify(job.json())

@api.route('/job/<job_id>', methods=['PUT'])
def update_job(job_id):
    # TODO: Implement a parser to ensure put data is received in the right format.
    data = request.get_json()
    job = job_service.update_job(job_id, data['data'], data['active'])
    return jsonify(job.json())

@api.route('/job/<job_id>', methods=['DELETE'])
def delete_job(job_id):
    job_service.remove_job(job_id)
    return jsonify({"message": "Job has been removed"})

@api.route('/<path>', methods=['GET','POST','PUT','DELETE','OPTIONS'])
def invalid_route(path):
    return jsonify({"error": "Invalid request"})