import os
def dofile(f): 
    if os.path.exists(f) == False:
        print("it does no exist")
        with open(f, "w") as myfile:
            myfile.write("it does exist ")
        
    else: 
        print('it does exist')
if __name__== '__main__':
    filen= r'C:\Users\nifem\Desktop\Ayo\python\myt.txt'
    dofile(filen)
