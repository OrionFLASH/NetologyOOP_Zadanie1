class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"

    def _calculate_avg_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return round(total / count, 1) if count > 0 else 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        return f"{super().__str__()}\nСредняя оценка за лекции: {avg_grade}"

    def _calculate_avg_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return round(total / count, 1) if count > 0 else 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return super().__str__()


def calculate_avg_hw_grade(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return round(total / count, 1) if count > 0 else 0


def calculate_avg_lecture_grade(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return round(total / count, 1) if count > 0 else 0


student1 = Student('Олег', 'Иванов', 'male')
student1.courses_in_progress += ['Разработчик', 'Дизайнер']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Анна', 'Петрова', 'female')
student2.courses_in_progress += ['Разработчик']
student2.finished_courses += ['Основы программирования']

lecturer1 = Lecturer('Петр', 'Смирнов')
lecturer1.courses_attached += ['Разработчик']

lecturer2 = Lecturer('Семен', 'Тутуев')
lecturer2.courses_attached += ['Дизайнер']

reviewer1 = Reviewer('Виктор', 'Леманов')
reviewer1.courses_attached += ['Разработчик']

reviewer2 = Reviewer('Василий', 'Теркин')
reviewer2.courses_attached += ['Дизайнер']

reviewer1.rate_hw(student1, 'Разработчик', 10)
reviewer1.rate_hw(student1, 'Разработчик', 7)
reviewer1.rate_hw(student2, 'Разработчик', 4)

student1.rate_lecturer(lecturer1, 'Разработчик', 7)
student1.rate_lecturer(lecturer1, 'Разработчик', 2)
student2.rate_lecturer(lecturer1, 'Разработчик', 9)

print(reviewer1)
print("---")
print(lecturer1)
print("---")
print(student1)
print("---")

print(student1 > student2)
print(lecturer1 == lecturer2)

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(f"Средняя оценка за домашние задания по курсу Разработчик: {calculate_avg_hw_grade(students, 'Разработчик')}")
print(f"Средняя оценка за лекции по курсу Разработчик: {calculate_avg_lecture_grade(lecturers, 'Разработчик')}")