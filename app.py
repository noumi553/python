from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "mysecretapikey123"

@app.route('/get-user', methods=['GET'])
def get_user():
    key = request.args.get('x-api_key')
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({
        "name": "Nouman Aziz",
        "email": "nouman@example.com"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
