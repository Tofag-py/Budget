name = input("Enter your name: ")
Gender = input("Are you Male or Female? ")
Marital_Status = input("Are you Married? ")
Dependent = int(input("How many dependents do you have? "))
debt_dues = int(input("Do you have any debt? If Yes, How much? "))
income = int(input("Enter your monthly income (Naira): "))
school_fees = int(input("Enter your child's school fees: "))


def rent():
    if income < 150000:
        Rent = 16.7 * income
    else:
        Rent = 0.25 * income
    return Rent

Rent = rent()

def Feed():
    adult = 20000
    if Dependent > 0:
        adult = 20000
        child = 0.5 * adult 
        gross_dependent = child * Dependent
    else:
        return adult

def Tax():
    tax = 0.17 * income
    return tax

def Debt():
    if debt_dues> 10000:
        debt = 0.1 * debt_dues
    return debt

def Transport():
    trans = 15000
    return trans

def HouseSup():
    housesupplies = 10000
    if income < 150000:
        if Dependent > 0:
            housesupplies *= Dependent
        else:
            pass
    else:
        if Dependent> 0:
            housesupplies = Dependent * 2.5
        else:
            pass
    return housesupplies

def Health():
    healthcare = 10000
    if Dependent>0:
        healthcare *= Dependent
    return healthcare

def Ed():
    if Dependent > 0:
        SchoolFees = (school_fees/3) * Dependent
    return SchoolFees

def Clothing():
    adult = 10000
    clothes = adult
    children = 1.5 * adult
    if Dependent>0:
        clothes = (children * Dependent)
    else:
        pass
    return clothes

def Save():
    savings = 0.1 * income
    return savings

def Urgent():
    Miscellanous = 30000
    return Miscellanous
     
tax = Tax()
feeding = Feed()
debt = Debt()
transport = Transport()
housesupplies = HouseSup()
health = Health()
education = Ed()
clothing = Clothing()
savings = Save()
miscellanous = Urgent()

print("Your tax is ", tax)
print("Your Feeding allocation should be ", feeding)
print("Your Debt repayment allocation should be ", debt)
print("Your transport allocation should be ", transport)
print("Your Household Supplies allocation should be ", housesupplies)
print("Your Health allocation should be ", health)
print("Your Education allocation should be ", education)
print("Your Clothing allocation should be ", clothing)
print("Your Savings should be ", savings)
print("Your Miscellanous should be ", miscellanous)
