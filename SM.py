class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other):
        if not isinstance (Student, other):
            print ('Ошибка')
        else:
            return self._average() < other._average()

    def __str__(self):
        return (f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания:{self._average()}\n Курсы в процессе изучения: {" ".join(self.courses_in_progress)}\n Завершенные курсы:{" ".join(self.finished_courses)}')

    def _average(self, grades):
        for key, value in self.grades:
            for value_grade in value:
                average_grade = sum(value_grade) / len(value_grade)

    def rate_lec(self,lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = grade
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    grades = {}
    def __str__(self):
        return (f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции:{self._average()}')

    def __lt__(self, other):
        if not isinstance (Lecturer, other):
            print ('Ошибка')
        else:
            return self._average() < other._average()

    def _average(self, grades):
        for key, value in grades:
            for value_grade in value:
                average_grade = sum(value_grade) / len(value_grade)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f'Имя: {self.name}\n Фамилия: {self.surname}')



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)