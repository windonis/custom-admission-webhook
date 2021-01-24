from flask import Flask, request, jsonify
from pprint import pprint
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def validate():
    allowed = True
    try:
        for container_spec in request.json["request"]["object"]["spec"]["containers"]:
            if "env" not in container_spec:
                allowed = False
    except KeyError:
        pass
    return jsonify(
        {
            "response": {
                "allowed": allowed,
                "uid": request.json["request"]["uid"],
                "status": {"message": "env keys are prohibited"},
            }
        }
    )

if __name__ == '__main__':
    app.run(debug=True)