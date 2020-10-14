from flask import Blueprint, jsonify, request
import rest_api.constants
from rest_api.services.job import JobService
from rest_api.services.request_validator import RequestValidator

api = Blueprint('api', __name__)
job_service = JobService()
validator = RequestValidator()

@api.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = job_service.get_all_jobs()
    return jsonify({"jobs": [job.json() for job in jobs]})

@api.route('/job', methods=['POST'])
def new_job():
    params = validator.validate_params(request.get_json(), ('data', 'active'))
    if not params:
        return invalid_route('', rest_api.constants.MESSAGE_INVALID_PARAMS)
    job = job_service.create_new_job(*params)
    return jsonify(job.json())

@api.route('/job/<job_id>', methods=['GET'])
def get_job(job_id):
    job = job_service.get_job(job_id)
    return jsonify(job.json())

@api.route('/job/<job_id>', methods=['PUT'])
def update_job(job_id):
    params = validator.validate_params(request.get_json(), ('data', 'active'))
    if not params:
        return invalid_route('', rest_api.constants.MESSAGE_INVALID_PARAMS)
    job = job_service.update_job(job_id, *params)
    return jsonify(job.json())

@api.route('/job/<job_id>', methods=['DELETE'])
def delete_job(job_id):
    job_service.remove_job(job_id)
    return jsonify({"message": "Job has been removed"})

@api.route('/<path>', methods=['GET','POST','PUT','DELETE','OPTIONS'])
def invalid_route(path, message=rest_api.constants.MESSAGE_INVALID_ENDPOINT, code=400):
    return jsonify({"error": message}), code