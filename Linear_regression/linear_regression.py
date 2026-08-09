import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
file_path = "house_price_small_dataset.csv" 
df = pd.read_csv(file_path)

# Extract features and target values
X = df["Size (sq ft)"]
y = df["Price ($)"]

# Number of data points
n = len(X)

# Calculate the slope (m) and intercept (b) for the linear regression line
m = (n * np.sum(X * y) - np.sum(X) * np.sum(y)) / (n * np.sum(X**2) - np.sum(X)**2)
b = (np.sum(y) - m * np.sum(X)) / n

print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")

# Predicted values using the regression line
y_pred = m * X + b

# Plot the data points
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color="blue", alpha=0.7, label="Actual Data")
plt.plot(X, y_pred, color="red", label="Regression Line")
plt.title("Linear Regression: Size (sq ft) vs. Price ($)")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)
plt.show()
