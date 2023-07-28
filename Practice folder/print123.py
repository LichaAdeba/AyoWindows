def threeNumberCombination(num):
    #create value you want to end at 
    calculate = 111 * int(num)
    #Set the calue of number equal to each other 
    if num == num:
        #create range for the the number using for loop and number you want to end at
        for i in range (111, calculate):
            #in order to end on range increase i loop by 1
            i = i+1
            #print i
            print(i)
if __name__=='__main__':
    #create input for number
    enter = input("input number: ")
    #call fucntion 
    threeNumberCombination(enter)