print ("Payroll Generator Mark III")
def HourlyWage():
    payrate = input("Enter your hourly rate:")
    try:
        payrate = float(payrate)
    except:
        print("Please enter a number:")
        payrate = -1
    return payrate
def HoursWorked():				
    hours = input("How many hours did you work?")
    try:
        hours = float(hours)
    except:
        print("Please enter a number:")
        hours = -1
    return hours
def PaidTimeOff():
    vacation = input("How many Vacation/PDO hours did you use?")
    try:
        vacation = float(vacation)
    except:
        print("Please enter a number:")
        vacation = -1
    return vacation
def Overtime(hours):
    if hours - 40 <= 0:
        overtime = 0
    else:
        overtime = (hours - 40) * (payrate * 1.5)
    return overtime
def Paycheck():
    wages = (hours + vacation) * payrate
    salary = overtime + wages
    print("Your gross pay is ${0} at the payrate of {1}".format(salary,payrate),"/hr.")
payrate = HourlyWage()
hours = HoursWorked()
vacation = PaidTimeOff()
overtime = Overtime(hours)
Paycheck()