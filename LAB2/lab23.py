def decimal_to_binary(n):
    if n == 0:
        return 0
    return n % 2 + 10 * decimal_to_binary(n // 2)

num = int(input("Enter a decimal number: "))
print(f"Binary: {decimal_to_binary(num)}")
