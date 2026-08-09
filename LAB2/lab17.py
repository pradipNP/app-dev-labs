
def average_of_three(a, b, c):
    return (a + b + c) / 3

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

average = average_of_three(num1, num2, num3)

print(f"The average of {num1}, {num2}, and {num3} is: {average}")
