def process():
    firstname = input("Please enter your first name: ")
    print("Thank you "+firstname)
    answer1= input(firstname+" do you like apples or pears? ")
    if answer1=="apples":
        print("I love apples too")
    else:
        print("I really dont like pears")

if __name__=="__main__":
    process()