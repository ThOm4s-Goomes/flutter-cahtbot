from flask import Flask, jsonify, request
import time

app = Flask(__name__)
@app.route("/bot", method=["POST"])

def response():
    query = dict(request.form)['query']
    result = query + "" + time.asctime()
    return jsonify({"response" : result})

if __name__ == "__main__":
    app.run("0.0.0.",)