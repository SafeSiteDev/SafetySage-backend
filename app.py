from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/test', methods=['GET'])
def test_endpoint():
    return jsonify({"message": "Hello from SafetySage backend!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
