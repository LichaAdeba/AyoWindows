
class Car(object):
    def __init__(self,brand,color, year_of_manifacture, mileage);
        self.brand = brand 
        self.color = color 
        self.year_of_manifacture = year_of_manifacture
        self.mileage = mileage

class Student(object):
    def __init__(self, name, age, grade, nationality):
        self.name = name 
        self.age = age 
        self.grade = grade
        self.nationality = nationality 
        print("The name of strudents is %s" % (self.name))
        print("The name of student is %s" % (self.age))
        print("The grade of student is %s"  % (self.grade))
        print("The nationality of student is %s" %(self.nationality.getcountry())) 

    def talk(self,say:)
        print(say)
    
    def study(self, hours):
        print("I am studying for %s hours" %(hours))

class Nationality(object):
    def __init__(self,country):
        self.country = country 

    def getcountry(self):
        print("I am a %s" %(self.country))

if __name__ =="__main__"
    american = Naitonality("American")
    ayokunle = student("Ayokunle", 16, 12, american)
    ayokunle.talk("Good evening I am earning to code ")
    ayokunle.study(10)
    ayokunle.getcountry