#using the os module find all the files in a directory and print it to the screen.
import os 
def folderAndFiles(f):
    for file in f:
        print(file)
    

if __name__=='__main__':
    folderafile = []    
    directory = r'C:\Users\nifem\Desktop\Ayo\python'
    files = os.listdir(directory)
    folderafile.append(files)
    folderAndFiles(files)
