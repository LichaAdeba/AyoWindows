from Demo import math

def calculateAreassides():
    print("Hello")

if __name__=="__main__":
    f = 22
    e = 7
    x = int(input("length of sides: "))
    
    sides = int(input("iput any number of sides: " ))
    
    d = math.calculateCircle(f,e,x)
    s = math.calculatesquare(x)
    t = math.calculatetriangle(x)
    c = math.calculateCube(x)
    
    if sides == 1:
        print("area of circle:" + str(d))
   
    elif sides == 4:
        print("area of square:"+ str(s))
    
    elif sides == 3:
        print("area of triangle:"+ str(t))
    
    elif sides == 6:
        print("are of cube:" + str(c))
    

    







    
    