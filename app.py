from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to connect to backend

@app.route('/')
def home():
    return "Welcome to the Carbon Cutters Backend!"

if __name__ == '__main__':
    app.run(debug=True)

