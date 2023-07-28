#create a python program that checks if a file exists and if not it creates it.
#N.B: use the os module to check if the file exists

import os
def dofile(x):
    if os.path.exists(x) == False:
        print("it does not exist")
        with open(x , "w") as myfile:
            myfile.write("I am content in file")
    else: 
        print("it exists")

if __name__ =="__main__":
    filename = r'C:\Users\nifem\Desktop\Ayo\python\mydemo.txt'
    dofile(filename)


    