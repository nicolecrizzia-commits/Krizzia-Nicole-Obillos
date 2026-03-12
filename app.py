from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api-home')
def home():
    return "Welcome to Krizzia Nicole Obillos' Flask API!"

@app.route('/student')
def get_student():
    return jsonify({
        "name": "Krizzia Nicole Obillos",
        "grade": 10,
        "section": "Zechariah"
    })

if __name__ == "__main__":
    app.run(debug=True)
