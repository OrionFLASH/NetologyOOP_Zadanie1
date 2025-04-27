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