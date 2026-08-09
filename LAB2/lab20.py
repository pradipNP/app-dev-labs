def sum_series(n):
    if n == 1:
        return 1
    return n + sum_series(n - 1)

n = int(input("Enter n: "))
print(f"Sum of series: {sum_series(n)}")
