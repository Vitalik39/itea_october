from abc import ABC, abstractmethod
from datetime import date

class Person(ABC):

    def __init__(self, surname, born, faculty):
        self.surname = surname
        self.born = born
        self.faculty = faculty


    @abstractmethod
    def info(self):
        pass


    def age(self):
        today = date.today()
        print(today.year - self.born)

    def search(self, startAge, endAge):
            today = date.today()
            if endAge > today.year - self.born > startAge:
                self.info()



class Enrollee(Person):

    def info(self):
        print(f'Surname of the enrollee {self.surname}, '
              f'enrollee birthday {self.born}, '
              f'faculty of the enrollee {self.faculty}.')


class Student(Person):

    def __init__(self, surname, born, faculty, course):
        super().__init__(surname, born, faculty)
        self.course = course


    def info(self):
        print(f'Surname of the student {self.surname}, '
              f'student birthday {self.born}, '
              f'faculty of the student {self.faculty}, '
              f'course of the student {self.course}.')

class Lecturer(Person):

    def __init__(self, surname, born, faculty, position, experience):
        super().__init__(surname, born, faculty)
        self.position = position
        self.experience = experience


    def info(self):
        print(f'Surname of the lecturer {self.surname}, '
              f'lecturer birthday {self.born}, '
              f'faculty of the lecturer {self.faculty}, '
              f'position of the lecturer {self.position}, '
              f'experience of the lecturer {self.experience}.')

list_ = [
    Student('Petrov', 2004, 'Economic', 1),
    Student('Esenin', 2002, 'Biological', 3),
    Student('Ivanov', 2001, 'Chemical', 4),
    Enrollee('Popov', 2005, 'Mathematical'),
    Enrollee('Pupkin', 2000, 'Welding'),
]

def display():
    for i in list_:
        i.info()

def check():
    lower_value = int(input('Enter the lower value: '))
    upper_value = int(input('Enter the upper value: '))
    for i in list_:
        i.search(lower_value, upper_value)
