class CalculateMonthlyBill(object):
    def __init__(self):
        self.familyname="Adebisi"
        self.waterpayment="0.0"
        self.electricitypayment="0.0"
        self.rentpayment ="0.0"
        self.carpayment = "0.0"
        self.insurancepayment = "0.0"

    def askForWaterPayment(self):
        self.waterpayment= input("enter your water payment:")
    def askForElectricityPayment(self):
        self.electricitypayment = input("enter your electricity payment:")
    def askForRentPayment(self):
        self.rentpayment =input("enter your rent payment:")
    def askForCarPayment(self):
        self.carpayment = input("enter your car payment:")
    def aksForInsurancePayment(self):
        self.insurancepayment = input("enter your isurance payment:")
    def setName(self, familyname):
        self.familyname = familyname 
    def getName(self):
        return self.familyname


    def generateTotal(self):
        YourTotal = float(self.waterpayment) + float(self.electricitypayment) +  float(self.rentpayment) + float(self.carpayment) + float(self.insurancepayment)
        print("your total is:" + str(YourTotal))


#def calculatemonthlyBill():

   # waterpayment= input("enter your water payment:")
    #print("your water payment is:" + waterpayment)
   # #electricitypayment = input("enter your electricity payment:")
    #print("your electricity payment is:" + electricitypayment )
   # rentpayment = input("enter your rent payment:")
    #print("your rent patment is:"+ rentpayment)
    #carPayment = input("enter your car payment:")
    #print("your car payment is:" + carPayment)
    #insurancepayment = input("enter your isurance payment:")
    #print("your insurance payment is:" + insurancepayment)
    #YourTotal = int(waterpayment) + int(electricitypayment) + int(rentpayment) + int(carPayment) + int(insurancepayment)
    #print("your total is:" + str(YourTotal))
if __name__=="__main__":
    #calculatemonthlyBill()
    ahh=CalculateMonthlyBill()
    ahh.askForWaterPayment()
    ahh.askForElectricityPayment()
    ahh.askForCarPayment()
    ahh.askForRentPayment()
    ahh.aksForInsurancePayment()
    ahh.generateTotal()