from Payment.calculateMonthlyBills import calculateMonthlyBills

if __name__=='__main__':
    Money = calculateMonthlyBills()
    print(Money.getName())
    Money.setName('Anybody')
    print(Money.getName())
    Money.aksForInsurancePayment()
    Money.askForElectricityPayment()
    Money.askForRentPayment()
    Money.askForCarPayment()
    Money.askForWaterPayment()
    Money.generateTotal()
