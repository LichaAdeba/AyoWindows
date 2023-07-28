#using the os module find all the files in a directory and print it to the screen.
import os 





if __name__=='__main__':  
    directory = r'C:\Users\nifem\Desktop\Ayo\python'

    for (roots,dir,files) in os.walk(directory, topdown=True):
        for f in files:
            print(roots+f)
            #print(dir)
    
    