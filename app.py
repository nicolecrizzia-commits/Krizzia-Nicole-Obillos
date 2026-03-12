from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
students = [
    {"id": 1, "name": "Krizzia Nicole Obillos", "grade": 10, "section": "Zechariah"},
    {"id": 2, "name": "Maria Santos", "grade": 10, "section": "Faith"}
]

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Student API",
        "developer": "Krizzia Nicole Obillos",
        "available_routes": [
            "/students - View all students",
            "/students/<id> - View one student",
            "/add_student - Add a new student (POST)"
        ]
    })

# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Get student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s["id"] == id), None)
    if student:
        return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

# Add a new student
@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()

    new_student = {
        "id": len(students) + 1,
        "name": data.get("name"),
        "grade": data.get("grade"),
        "section": data.get("section")
    }

    students.append(new_student)

    return jsonify({
        "message": "Student added successfully",
        "student": new_student
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
