import math 
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly pay rate: "))
federalTax = float(input("Enter tax withholding rate: "))
stateTax = float(input("Enter state tax withholding rate: "))

pay = hours * rate
Tax = pay * federalTax #зарплата после вычетов налогов федеративныых 
stTax = pay * stateTax # зарплата после вычетов налогов штатных
payTax = pay - Tax - stTax # зарплата после вычетов налогов


print (f"Employee Name: {name}")
print (f"number of hours: {hours}")
print (f"Pay Rate: {rate}")
print (f"Federal Tax: {federalTax}")    
print (f"State Tax: {stateTax}")

print (f"Payment: {payTax}")