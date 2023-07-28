import os 
def folderAndFiles(f):
    for file in f:
        print(f)

if __name__=='__main__':
    folderafile = []    
    directory = r'C:\Users\nifem\Desktop\Ayo\python'
    files = os.listdir(directory)
    folderafile.append(files)
    folderAndFiles(files)
