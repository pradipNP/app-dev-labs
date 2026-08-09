def simple_interest(p, t, r=10):
    return (p * t * r) / 100

principal = float(input("Enter principal amount: "))
time = float(input("Enter time (in years): "))
rate = input("Enter rate (press Enter for default 10%): ")

if rate:
    print(f"Simple Interest: {simple_interest(principal, time, float(rate)):.2f}")
else:
    print(f"Simple Interest: {simple_interest(principal, time):.2f}")
