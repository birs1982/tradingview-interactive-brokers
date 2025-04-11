from flask import Flask, request, jsonify

app = Flask(__name__)  # <== This is the 'app' gunicorn is looking for

@app.route('/')
def home():
    return "It works!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received:", data)
    return jsonify({"status": "received"})
