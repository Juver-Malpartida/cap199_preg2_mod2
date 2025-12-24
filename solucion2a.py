
import numpy as np
import matplotlib.pyplot as plt

# 1. Define the sine function
def f(x):
    return np.sin(x)

# 2. Define the derivative of the sine function (cosine)
def df(x):
    return np.cos(x)

# 3. Choose the points for the tangents
points = [0, np.pi/4, np.pi/2, np.pi, 3*np.pi/2]

# Generate x values for plotting the sine curve
x_sin = np.linspace(-0.5, 2 * np.pi + 0.5, 400)
y_sin = f(x_sin)

plt.figure(figsize=(10, 6))

# Plot the sine function
plt.plot(x_sin, y_sin, label='sin(x)', color='blue')

# Plot tangent lines at specified points
for x_point in points:
    y_point = f(x_point)
    slope = df(x_point)

    # Equation of the tangent line: y - y1 = m * (x - x1)
    # y = m * (x - x1) + y1
    x_tangent = np.linspace(x_point - 1, x_point + 1, 100)
    y_tangent = slope * (x_tangent - x_point) + y_point

    plt.plot(x_tangent, y_tangent, '--', label=f'Tangente en x={x_point:.2f}', alpha=0.7)
    plt.plot(x_point, y_point, 'o', color='red') # Mark the tangent point

plt.title('Función Seno con Rectas Tangentes')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.ylim(-2, 2)
plt.xlim(-0.5, 2 * np.pi + 0.5)
plt.show()
