from abc import ABC, abstractmethod


class Student(ABC):
    school = "ABC School"                         # Class Variable

    def __init__(self, name, age, course, marks): # Constructor
        self.name = name                          # Instance Variable
        self.age = age
        self.course = course
        self.__marks = marks                      # Encapsulation / Private

    @abstractmethod
    def display(self):                            # Abstraction
        pass

    def show(self):                               # Instance Method
        print(self.name)
        print(self.age)
        print(self.course)

    def info(self, *args):                        # Method Overloading approach
        print(args)

    def __add__(self, other):                     # Operator Overloading
        return self.marks + other.marks

    @classmethod
    def change_school(cls, school):               # Class Method
        cls.school = school

    @staticmethod
    def message():                                # Static Method
        print("I like Java")

    @property
    def marks(self):                              # Getter
        return self.__marks

    @marks.setter
    def marks(self, value):                       # Setter + Validation
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks")


class GraduateStudent(Student):                   # Inheritance

    def __init__(self, name, age, course, marks, specialization):
        super().__init__(name, age, course, marks) # super()
        self.specialization = specialization

    def display(self):                            # Abstract Method implementation
        print("Graduate Student")

    def show(self):                               # Method Overriding
        super().show()
        print(self.specialization)


class Teacher:                                    # Duck Typing
    def show(self):
        print("Teacher Profile")


def display_student(student):                      # Polymorphism
    student.show()


g1 = GraduateStudent("Rahul", 22, "MCA", 85, "Python")
g2 = GraduateStudent("Amit", 24, "MCA", 80, "Python")

# Class Variable
print(g1.school)

# Class Method
Student.change_school("XYZ School")
print(g1.school)

# Static Method
g1.message()

t1 = Teacher()

# Student information
print(g1.name)
print(g1.marks)

g1.show()

# Abstraction
g1.display()

# Polymorphism + Duck Typing
display_student(g1)
display_student(t1)

# Operator Overloading
total = g1 + g2
print("Total Marks:", total)

# Setter + Validation
g1.marks = 95
print("New Marks:", g1.marks)

g1.marks = 150
print("Marks:", g1.marks)

# isinstance / issubclass
print(isinstance(g1, GraduateStudent))
print(isinstance(g1, Student))
print(issubclass(GraduateStudent, Student))

# Method Overloading approach
g1.info()
g1.info("Rahul")
g1.info("Rahul", 22, "MCA")
