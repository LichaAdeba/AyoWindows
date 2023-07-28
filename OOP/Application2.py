from Inheritance.daughter import daughter

if __name__=='__main__':
    diana = daughter('beans','baby','Prepare kids for school')
    print(diana.getPlan())
    diana.setPlan('Prepare Doctors appointment')
    print(diana.getPlan())