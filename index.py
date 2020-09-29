from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/jobs', methods=['GET'])
def get_jobs():
    return jsonify({"jobs": [1,2,3,4]})

@app.route('/job', methods=['POST'])
def new_job():
    return "new job created", 201

@app.route('/job/<job_id>', methods=['GET'])
def get_job(job_id):
    return jsonify({"name": job_id})

@app.route('/job/<job_id>', methods=['PUT'])
def update_job(job_id):
    return "Job updated"

@app.route('/job/<job_id>', methods=['DELETE'])
def delete_job(job_id):
    return "Job deleted"

@app.route('/<path>', methods=['GET','POST','PUT','DELETE','OPTIONS'])
def invalid_route(path):
    return jsonify({"error": "Invalid request"})

app.run(port=5000, debug=True)