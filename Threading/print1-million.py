import time

def cong():
    for i in range(1,1000000):
        print(i)

if __name__=='__main__':
    starttime = time.time()
    cong()
    finishtime = time.time()
    programtime = finishtime - starttime
    print(str(programtime))