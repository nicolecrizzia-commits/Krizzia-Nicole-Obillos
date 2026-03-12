from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/api-home', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to Krizzia Nicole Obillos' Flask API!",
        "routes": [
            "/api-home",
            "/student"
        ]
    })

# Student route
@app.route('/student', methods=['GET'])
def get_student():
    return jsonify({
        "name": "Krizzia Nicole Obillos",
        "grade": 10,
        "section": "Zechariah"
    })

if __name__ == "__main__":
    app.run()
