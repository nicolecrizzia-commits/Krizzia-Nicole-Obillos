from flask import Flask, jsonify, request

app = Flask(__name__)

# Updated home route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Krizzia Nicole Obillos' Flask API",
        "available_routes": [
            "/",
            "/student",
            "/grade"
        ]
    })

# Student information route
@app.route('/student')
def get_student():
    return jsonify({
        "name": "Krizzia Nicole Obillos",
        "grade": 10,
        "section": "Zechariah"
    })

# New grade route
@app.route('/grade')
def grade():
    return jsonify({
        "subject": "Web Development",
        "score": 95,
        "status": "Passed"
    })

if __name__ == "__main__":
    app.run(debug=True)
