class Person():
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def toString(self):
        return(f"{self.name}({self.address})")


class Student(Person):
    def __init__(self, name, address, numCourses = 0, courses = [], grades = []):
        super().__init__(name, address)
        self.numCourses = numCourses
        self.courses = courses
        self.grades = grades
    
    def addCourseGrade(self, course, grade):
        self.courses.append(course)
        self.grades.append(grade)

    def printGrades(self):
        print(self.grades)

    def AverageGrade(self):
        return(sum(self.grades)/(len(self.grades)))

    def __str__(self):
        return (f"Name: {self.name}\n Address: {self.address}")

class Teacher(Person):

    def __init__(self, name, address, numCourse =  0, courses  = []):
        super().__init__(name, address)
        self.numCourse = numCourse
        self.courses = courses

    def addCourse(self, course):
        for courses in self.courses:
            if course == courses:
                return False
        self.courses.append(course)
        return True
    
    def removeCourse(self, course):
        if course in self.courses:
            self.courses.remove(course)
            return True
        else:
            return False

    def __str__(self):
        return(f"Name:  + {self.getName()}\nAddress: {self.getAddress()}")
