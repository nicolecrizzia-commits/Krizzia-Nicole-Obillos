from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory students list (this will reset when the server restarts)
students = [
    {"id": 1, "name": "Krizzia Nicole Obillos", "grade": 10, "section": "Zechariah"},
    {"id": 2, "name": "John Cruz", "grade": 10, "section": "Matthew"},
    {"id": 3, "name": "Maria Santos", "grade": 10, "section": "Luke"}
]

# Home route
@app.route('/api-home', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to Krizzia Nicole Obillos' Flask API!",
        "routes": [
            "/api-home",
            "/students [GET]",
            "/students [POST]",
            "/students/<id> [GET, PUT, DELETE]"
        ]
    })

# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Get a single student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        return jsonify(student)
    else:
        abort(404, description="Student not found")

# Create a new student
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if not data or "name" not in data or "grade" not in data or "section" not in data:
        abort(400, description="Missing required fields")
    
    new_id = max([s["id"] for s in students]) + 1 if students else 1
    new_student = {
        "id": new_id,
        "name": data["name"],
        "grade": data["grade"],
        "section": data["section"]
    }
    students.append(new_student)
    return jsonify(new_student), 201

# Update an existing student
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        abort(404, description="Student not found")

    data = request.get_json()
    student["name"] = data.get("name", student["name"])
    student["grade"] = data.get("grade", student["grade"])
    student["section"] = data.get("section", student["section"])
    return jsonify(student)

# Delete a student
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        abort(404, description="Student not found")
    
    students = [s for s in students if s["id"] != student_id]
    return jsonify({"message": f"Student {student_id} deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
