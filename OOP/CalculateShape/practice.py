class Triangle(Shape):
    def __init__(self,numsides):
        super().__init__(numsides)
    def getArea(self,length=None,width=None):
        if length and width:
            return (0.5 * width) * length 
class Circle(Shape):
    def __init__(self,numsides):
        super().__init__(numsides)
    def getArea(self, x=None ,y=None,r=None):
            if x and  y and r:
                return  (x/y) * (r * r)
class Rectangle(Shape):
    def __init__(self,numsides):
        super().__init__(numsides)
    def getArea(self, length, width):
        if length and width:
            return length * width


    print(square.getArea(10))
    triangle = Triangle(3)
    triangle.getArea()
    print(triangle.getArea(2 ,3 ))
    circle = Circle(1)
    circle.getArea()
    print(circle.getArea(22,7,4))

    rect = Rectangle(4)
    rect.getArea()
    print(rect.getArea(10, 3))