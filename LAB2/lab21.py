def reverse_recursive(n):
    if n < 10:
        return n
    return int(str(n % 10) + str(reverse_recursive(n // 10)))

num = int(input("Enter a number: "))
print(f"Reversed number: {reverse_recursive(num)}")
