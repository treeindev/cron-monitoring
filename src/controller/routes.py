from flask import Blueprint, jsonify, request
from core.job_manager import JobManager
from utils.constants import RESPONSE_MESSAGES

api = Blueprint("cronmonitoring_rest_api", __name__)
job_manager = JobManager()

@api.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        jobs = job_manager.get_jobs()
        collection = []
        for job in jobs:
            collection.append(job.__dict__)
        return jsonify(collection)
    except:
        return (jsonify({"Error": RESPONSE_MESSAGES["INTERNAL_ERROR_JOBS"]}), 500)

@api.route('/job', methods=['POST'])
def create_job():
    try:
        params = request.get_json()

        job_manager.add_job(
            params["minutes"],
            params["hours"],
            params["days"],
            params["month"],
            params["week_day"],
            params["location"],
            params["execution"],
            params["output"],
            params["error"]
        )
        return (jsonify({"Message": "New job created"}), 201)
    except:
        return (jsonify({"Error": RESPONSE_MESSAGES["GENERAL_ERROR_PARAMS"]}), 400)

@api.route('/job', methods=['DELETE'])
def delete_job():    
    try:
        params = request.get_json()

        job_manager.remove_job(params["id"])
        return (jsonify({"Message": RESPONSE_MESSAGES["JOB_REMOVED_SUCCESS"]}), 200)
    except:
        return (jsonify({"Error": RESPONSE_MESSAGES["GENERAL_ERROR_PARAMS"]}), 400)

@api.route('/<path>', methods=['GET', 'POST', 'DELETE'])
def invalid_request(path):
    return (jsonify({"Error": RESPONSE_MESSAGES["GENERAL_ERROR_ROUTE"]}), 404)