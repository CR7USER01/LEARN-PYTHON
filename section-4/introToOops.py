my_student = {
    'name': 'jitu',
    'grades': [70, 88, 90, 34],
    'average': None #something here
}

def average_grade(student):
    return sum(student['grades'])/len(student['grades'])

#print(average_grade(my_student))

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

        def average(Self):
         return sum(self.grades)/ len(self.grade)
    

student_one = Student('Jitu', [70, 88, 90, 34])
student_two = Student('biswa', [75, 85, 93, 39])


print(student_two.name)
print(student_one.name)
    

