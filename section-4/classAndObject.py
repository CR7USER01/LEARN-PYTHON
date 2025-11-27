my_student = {
    'name': 'jitu',
    'grades': [70, 88, 90, 34],
    'average': None
}

def average_grade(student):
    return sum(student['grades'])/len(student['grades'])

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):   # FIXED
        return sum(self.grades)/ len(self.grades)
    

student_one = Student('Jitu', [70, 88, 90, 34])
student_two = Student('biswa', [75, 85, 93, 39])

print(student_one.average())
