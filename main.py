class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer,Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and grade <=10:
            lecturer.grades.append(grade)
        else:
            return "Ошибка"

    def avg_grade(self):
        sum_hw = 0
        count = 0
        for grades in self.grades.values():
            sum_hw += sum(grades)
            count += len(grades)
        return round(sum_hw / count, 1)

    def __str__(self):
        pri = f"Имя: {self.name}\nФамилия:{self.surname}\nСредняя оценка за ДЗ: {self.avg_grade()}"
        return pri

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Это не студент")
            return
        return sum(self.grades) / len(self.grades) > sum(other.grades) / len(other.grades)





class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = []
        self.courses_attached = []

    def __str__(self):
        pri = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {round(sum(self.grades) / len(self.grades), 1)}"
        return pri

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Это не преподователь")
            return
        return sum(self.grades) / len(self.grades) < sum(other.grades) / len(other.grades)

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def get_avg_hw_grade(student_list, course):
    total = 0
    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
                total += sum(grades)/len(grades)
    return round(total/len(student_list),1)

def get_avg_lec_grade(lec_list):
    total = 0
    for lecturer in lec_list:
        total += sum(lecturer.grades)/len(lecturer.grades)
    return total/len(lec_list)

student_Andrey = Student('Ruoy', 'Eman', 'man')
student_Andrey.courses_in_progress += ['Python']
student_Andrey.courses_in_progress += ['Git']
student_Andrey.finished_courses += ["Введение в программирование"]

student_Anna = Student('Anna', 'Types', 'girl')
student_Anna.courses_in_progress += ['Python']
student_Anna.courses_in_progress += ['Git']
student_Anna.finished_courses += ["Введение в базы данных"]

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']
student_Andrey.rate_lec(cool_lecturer, 'Python', 10)
student_Andrey.rate_lec(cool_lecturer, 'Python', 8)

bad_lecturer = Lecturer('Oleg', 'Maimi')
bad_lecturer.courses_attached += ['Python']
student_Anna.rate_lec(bad_lecturer, 'Python', 5)
student_Andrey.rate_lec(bad_lecturer, 'Python', 7)

cool_Reviewer = Reviewer('Some', 'Buddy')
cool_Reviewer.courses_attached += ['Python']

cool_Reviewer.rate_hw(student_Andrey, 'Python', 10)
cool_Reviewer.rate_hw(student_Andrey, 'Python', 5)
cool_Reviewer.rate_hw(student_Andrey, 'Git', 10)
cool_Reviewer.rate_hw(student_Anna, 'Python', 7)
cool_Reviewer.rate_hw(student_Anna, 'Python', 5)
cool_Reviewer.rate_hw(student_Anna, 'Git', 8)



print(get_avg_hw_grade([student_Anna, student_Andrey],'Python'))

print(get_avg_lec_grade([bad_lecturer,cool_lecturer]))