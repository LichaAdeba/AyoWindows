from CalculateShape.Shape import Shape 
class Rectangle(Shape):
    def __init__(self,numsides):
        super().__init__(numsides)
    def getArea(self, length = None, width = None):
        if length and width:
            return length * width
        else:
            return self.getArea()
class Square(Shape):
    def __init__(self,numsides):
        super().__init__(numsides)
    def getArea(self,length=None):
        if length:
            return length * 2
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

    

    
    

