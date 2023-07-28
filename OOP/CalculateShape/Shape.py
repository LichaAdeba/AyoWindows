class Shape(object):
    def __init__(self, numsides ):
        self.numsides = numsides
    def getArea(self):
        if self.numsides==1:
            print("Likely  a circle")
        if self.numsides==3:
            print("Likely a triangle")
        if self.numsides==4:
            print("Likely a square or rectangle")



