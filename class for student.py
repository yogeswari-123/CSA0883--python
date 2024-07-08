class Student:
    def __init__(self, name, marks_subject1, marks_subject2):
        self.name = name
        self.marks_subject1 = marks_subject1
        self.marks_subject2 = marks_subject2
    
    def calculate_average(self):
        return (self.marks_subject1 + self.marks_subject2) / 2


student1 = Student("anju", 90,67)
student2 = Student("abhi", 89,98)


print(f"{student1.name}'s average marks: {student1.calculate_average()}")
print(f"{student2.name}'s average marks: {student2.calculate_average()}")
