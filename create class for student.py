class Student:
    def _init_(self, name, mark_subj1, mark_subj2, mark_subj3):
        self.name = name
        self.mark_subj1 = mark_subj1
        self.mark_subj2 = mark_subj2
        self.mark_subj3 = mark_subj3

    def total_marks(self):
        return self.mark_subj1 + self.mark_subj2 + self.mark_subj3

student1 = Student("vyshu", 90, 60, 80)
student2 = Student("anju", 85, 60, 75)

total_marks_student1 = student1.total_marks()
total_marks_student2 = student2.total_marks()

print(f"Total marks for {student1.name}: {total_marks_student1}")
print(f"Total marks for {student2.name}: {total_marks_student2}")
