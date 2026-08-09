
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return reversed_num

n = int(input("Enter a number: "))

reversed_num = reverse_number(n)

print(f"The reversed number is: {reversed_num}")
