from CalculateShape.shape2 import *
if __name__=='__main__':
    rect = Rectangle(4)
    rect.getArea()
    print(rect.getArea(10, 3))
    square = Square(4)
    square.getArea()
    print(square.getArea(10))
    triangle = Triangle(3)
    triangle.getAreas()
    print(triangle.getArea(2 ,3 ))
    circle = Circle(1)
    circle.getArea()
    print(circle.getArea(22,7,4))


    