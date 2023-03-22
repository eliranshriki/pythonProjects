student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
for key in student_scores:
    student_grades[key] = student_scores[key]
    if student_grades[key]>90:
        student_grades[key]="outstanding"
    elif student_grades[key]>80:
        student_grades[key]="Exceeds Expectations"
    elif student_grades[key]>70:
        student_grades[key]="Acceptable"
    else:
        student_grades[key]="Fail"


print(student_grades)