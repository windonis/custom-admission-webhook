from flask import Flask, request, jsonify
from pprint import pprint
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    allowed = True
    request_info = request.json
    pprint(request_info)
     # for container_spec in request_info
    for container_spec in request_info["request"]["object"]["spec"]["containers"]:
         if 'env' not in container_spec:
             print("Environment Variables Cannot Be Passed to Containers")
             allowed = False

    admission_response = {
        "allowed": allowed
    }
    admissionReview = {
        "response": admission_response
    }
    return jsonify(admissionReview)


if __name__ == '__main__':
    app.run(debug=True)
