import time
def cong():
    for i in range(1,1000):
        print(i)
        for x in range(1000):
            print("")

if __name__=='__main__':
    starttime = time.time()
    cong()
    finishtime = time.time()
    programtime = finishtime - starttime
    print(str(programtime)) 