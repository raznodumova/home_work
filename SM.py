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
        result = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания:{self._average()}\n Курсы в процессе изучения: {" ".join(self.courses_in_progress)}\n Завершенные курсы:{" ".join(self.finished_courses)}'
        return result

    def _average(self):
        for key, value in self.grades:
            for value_grade in value:
                average_grade = sum(value_grade) / len(value_grade)


    def rate_lec(self,lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    grades = {}
    def __str__(self):
        result = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции:{self._average()}'
        return result

    def __lt__(self, other):
        if not isinstance (Lecturer, other):
            print ('Ошибка')
        else:
            return self._average() < other._average()

    def _average(self, grades):
        for key, value in grades:
            for value_grade in value:
                average_grade = sum(value_grade) / len(value_grade)
        return average_grade

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
        result = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return result


# ---------------------------------------------------------------------

student_1 = Student('Павел', 'Петров', 'm')
student_1.finished_courses += ['C+']
student_1.courses_in_progress += ['Python']

student_2 = Student('Ирина', 'Иванова', 'f')
student_2.finished_courses += ['JavaScript']
student_2.courses_in_progress += ['Python']

lecturer_1 = Lecturer('Светлана', 'Светланова')
lecturer_1.courses_attached += ['Python', 'JavaScript']

lecturer_2 = Lecturer('Тимур', 'Тимуров')
lecturer_2.courses_attached += ['C+', 'Python']

reviewer_1 = Reviewer('Алтай', 'Уралов')
reviewer_1.courses_attached += ['Python', 'C+']

reviewer_2 = Reviewer('Кубань', 'Донская')
reviewer_2.courses_attached += ['Python']

# -------------------------------------------------------------------

student_1.rate_lec(lecturer_1, 'Python', 10)
student_1.rate_lec(lecturer_2, 'Python', 9)

student_2.rate_lec(lecturer_1, 'Python', 9)
student_2.rate_lec(lecturer_2, 'Python', 10)

reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 8)

reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 10)

# --------------------------------------------------------------------

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]

def global_avarage_student(student_list, course):
    summ = 0
    quan = 0
    for stud in student_list:
        for crs in stud.grades.keys():
            if crs == course:
                summ += sum(stud.grades[course])
                quan += len(stud.grades[course])
        result = round(summ / quan, 2)
        summ += result
        quan += 1
    result_glb = round(summ / quan, 2)
    return result_glb

def global_avarage_lecturer(lecturer_list, course):
    summ = 0
    quan = 0
    for lect in lecturer_list:
        for crs in lect.grades.keys():
            if crs == course:
                summ += sum(lect.grades[course])
                quan += len(lect.grades[course])
        result = round(summ / quan, 2)
        summ += result
        quan += 1
    result_glb = round(summ / quan, 2)
    return result_glb

print('Студенты:')
print(student_1)
print(student_2)
print('Лекторы:')
print(lecturer_1)
print(lecturer_2)
print('Проверяющие:')
print(reviewer_1)
print(reviewer_2)
print(f'Сравнение результатов студентов:')
print(f'student_1 > student_2:{student_1 > student_2}')
print(f'Сравнение результатов лекторов:')
print(f'lecturer_1 > lecturer_2:{lecturer_1 > lecturer_2}')

