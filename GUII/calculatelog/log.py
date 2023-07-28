import math 

def isPrime(g):
    for i in range(2, 2<=g,g):
        if (g % i == 0):
            return False
    return True 
def isPrime2(f):
    for i in range(2, 2<=f, f):
        if (f % i == 0):
            return False
    return True 
if __name__=="__main__":
    x = 2 
    n = 2 
    e = 2
    d = int(input("add number: "))
    while ((x)<=(d)):
        e=e+1
        total = 0
        n= math.log(e, 10)
        isprime = isPrime(n)
        isprime2 = isPrime2(e)
        if (isprime and isprime2): 
            if(x ==d): 
            
                print ("The value of prime number: " + str(e))
        x = x+1

        print("The value of log: " + str(n))
    total = int(total + n)        
    print("The total of log: "+ str(total))