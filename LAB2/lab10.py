number = int(input("Enter a number: "))
ans = 1
for i in range(1, number + 1):
    ans *= i

print(f"Factorial of {number} is {ans}")

