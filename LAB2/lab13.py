def is_perfect(n):
    sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i
            if i != n / i:
                sum += n / i
    return sum == n

num = int(input("Enter a number: "))
if is_perfect(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")
