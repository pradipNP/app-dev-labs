import math

def calculate_stats(a, b, c, d, e):
    # Calculate sum
    total_sum = a + b + c + d + e
    
    # Calculate average
    average = total_sum / 5
    
    # Calculate standard deviation
    variance = ((a - average) ** 2 + (b - average) ** 2 + (c - average) ** 2 + (d - average) ** 2 + (e - average) ** 2) / 5
    std_deviation = math.sqrt(variance)
    
    # Display results
    print(f"Sum: {total_sum:.2f}")
    print(f"Average: {average:.2f}")
    print(f"Standard Deviation: {std_deviation:.2f}")

# Example usage
a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
c = float(input("Enter number 3: "))
d = float(input("Enter number 4: "))
e = float(input("Enter number 5: "))

calculate_stats(a, b, c, d, e)
