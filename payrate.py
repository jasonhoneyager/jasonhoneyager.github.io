print ("Payroll Generator Mark V")
def HourlyWage():
    complete = False
    while not complete:
        payrate = input("Enter your hourly rate:")
        try:
            payrate = float(payrate)
            if payrate == 0:
                print("I highly doubt you work for free...")
                continue
            complete = True
        except:
            print("Please enter a number:")
    return payrate
def HoursWorked():
    complete = False
    while not complete:
        hours = input("How many hours did you work?")
        try:
            hours = float(hours)
            complete = True
        except:
            print("Please enter a number:")
    return hours
def PaidTimeOff():
    complete = False
    while not complete:
        vacation = input("How many Vacation/PDO hours did you use?")
        try:
            vacation = float(vacation)
            complete = True
        except:
            print("Please enter a number:")
    return vacation
def Overtime(hours):
    if hours - 40 <= 0:
        overtime = 0
    else:
        overtime = (hours - 40) * (payrate * 0.5)
    return overtime
def Paycheck():
    wages = (hours + vacation) * payrate
    salary = overtime + wages
    print("Your gross pay is ${0} at the payrate of ${1}".format(salary,payrate),"/hr.")
payrate = HourlyWage()
hours = HoursWorked()
vacation = PaidTimeOff()
overtime = Overtime(hours)
Paycheck()