number = int(input("Enter a 3-digit number: "))
number_str = str(number)

if number_str == number_str[::-1]:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
