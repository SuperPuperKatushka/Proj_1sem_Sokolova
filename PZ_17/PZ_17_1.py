# Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
# Добавьте методы для вычисления среднего балла и определения, является ли студент
# отличником/

class Student:
    def __init__(self, name, last_name, marks1, marks2, marks3 ):
        self.name = name
        self.last_name = last_name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def gpa(self):
        self.result = (self.marks1 + self.marks2 + self.marks3) / 3
        self.result_text = "Средний балл у Студента", self.name, self.last_name, ':', self.result
        self.string = ''
        for i in self.result_text:
            self.string += str(i)
            self.string += ' '
        return self.string

    def the_best(self):
        self.string_1 = ''
        if self.result >= 4.5:
            self.result_text_victory = "Студент ", self.name, self.last_name, "отличник!"
            for i in self.result_text_victory:
                self.string_1 += str(i)
                self.string_1 += ' '
            return self.string_1
        else:
            self.result_text_fail = "Студент ", self.name, self.last_name, ", к сожалению, не отличник!"
            for i in self.result_text_fail:
                self.string_1 += str(i)
                self.string_1 += ' '
            return self.string_1


StudentOne = Student("Игорь", "Самойлов", 5, 4, 2)
print(StudentOne.gpa())
print(StudentOne.the_best())

