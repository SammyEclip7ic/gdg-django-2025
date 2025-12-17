student_grades = {
    "Samrawit": 89,
    "Nahom": 90,
    "Natnael": 78,
    "Michael": 65
}

def get_grade(student_grades, student_name):
    try:
        return student_grades[student_name]
    except KeyError:
        return "Student not found in the system"
    
student = get_grade(student_grades, "Samuel")
print(student)