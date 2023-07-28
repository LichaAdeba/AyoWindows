def calculatePi(x,y):
    return (x/y)
def calculateDiameter(c,e):
    return (c / e)
if __name__== "__main__":
    c = 20 
    x = 22
    y = 7
    e = calculatePi(x,y)
    z = calculateDiameter(c, e)
    print("The diameter of a circle:" + str(z))
