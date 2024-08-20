import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Hours studied, reshaped to column vector
Y = np.array([50, 55, 65, 70, 75])           # Exam scores

# Create and fit the model
model = LinearRegression()
model.fit(X, Y)

# Coefficients
beta_0 = model.intercept_
beta_1 = model.coef_[0]

print(f"Intercept (beta_0): {beta_0}")
print(f"Slope (beta_1): {beta_1}")

# Predict
Y_pred = model.predict(X)

# Plot
plt.scatter(X, Y, color='orange', label='Actual scores')
plt.plot(X, Y_pred, color='green', label='Regression line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.legend()
plt.show()
