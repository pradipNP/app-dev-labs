def fibonacci(n):
   if n < 2:
       return n
   return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the value of n: "))
print(f"The {n}th fibonacci number is {fibonacci(n)}")
