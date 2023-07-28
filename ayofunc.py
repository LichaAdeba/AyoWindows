from Demo import math

def ayofunc():
    print("world cup")

if __name__=="__main__":
    x = 22 
    y = 7
    p = math.dividepi(x,y)
    d = math.divide(x,p)
    r = math.multiply(x,y)
    
    print("The value of pi:" + str(p))
    print("The value of a circumference:"+ str(d))
    print("The value of area of a rectangle:" + str(r))
    