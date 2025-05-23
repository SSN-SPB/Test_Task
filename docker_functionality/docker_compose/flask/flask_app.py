from flask import Flask, jsonify, request
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/', methods=['GET'])
def index():
    return jsonify(message="Hello from the REST API!"), 200

@app.route('/redis')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'),'utf-8')
    return "This webpage has been viewed "+counter+" time(s)"

@app.route('/home')
def home():
    return "Hello, World!"

@app.route('/view')
def view():
    return "What a view!"

@app.route('/data', methods=['POST'])
def handle_post():
    data = request.get_json()
    return jsonify(
        received=True,
        you_sent=data
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)