marks = {
    'student1': {'bio': 85, 'social': 90, 'hindi': 75},
    'student2': {'ethics': 80, 'english': 85, 'python': 90},
    'student3': {'maths': 70, 'science': 65, 'compiler': 80}
}
for student, subjects in marks.items():
    total_marks = sum(subjects.values())
    print(f"Total marks for {student}: {total_marks}")
