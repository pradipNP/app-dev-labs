
P = float(input("Enter the principal amount (P): "))
T = float(input("Enter the time in years (T): "))
R = float(input("Enter the annual interest rate (R) in percentage: "))

rate = R / 100

compound_interest = P * ((1 + rate) ** T - 1)

print("The compound interest is:", compound_interest)
