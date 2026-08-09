def sum_squares(n):
    if n == 1:
        return 1
    return n * n + sum_squares(n - 1)

n = int(input("Enter n: "))
print(f"Sum of squares: {sum_squares(n)}")
