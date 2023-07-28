from multiprocessing import Pool
import time


def printToConsole(i):
    return "current number is "+str(i)

if __name__=="__main__":
    starttime= time.time()
    with Pool(8) as pool:
        for result in pool.map(printToConsole,range(1000000)):
            print(result)

    finishtime=time.time()
    programtime= finishtime - starttime;
    print("Program completed in %s" %(str(programtime)))