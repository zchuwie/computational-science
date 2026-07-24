# Scientific Python Cheatsheet: NumPy, Matplotlib, SciPy

## 1. NumPy (Numerical Python)
*Core library for multi-dimensional arrays and mathematical operations.*

**Import:**
```python
import numpy as np
```

**Creating Arrays:**
```python
a = np.array([1, 2, 3])          # 1D array
b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float) # 2D array
c = np.zeros((3, 4))             # 3x4 array of zeros
d = np.ones((2, 3, 4))           # 2x3x4 array of ones
e = np.arange(10, 25, 5)         # Array of evenly spaced values (step) [10, 15, 20]
f = np.linspace(0, 2, 9)         # Array of evenly spaced values (number of samples)
```

**Array Properties:**
```python
a.shape         # Dimensions (e.g., (3,))
len(a)          # Length of array
b.ndim          # Number of dimensions (e.g., 2)
b.size          # Number of elements (e.g., 6)
b.dtype         # Data type of elements
```

**Math Operations:**
```python
a + b           # Element-wise addition (np.add(a, b))
a - b           # Element-wise subtraction (np.subtract(a, b))
a * b           # Element-wise multiplication (np.multiply(a, b))
a / b           # Element-wise division (np.divide(a, b))
np.exp(a)       # Exponentiation
np.sqrt(a)      # Square root
np.sin(a)       # Sine
np.cos(a)       # Cosine
a.dot(b)        # Dot product
```

**Aggregate Functions:**
```python
a.sum()         # Array-wise sum
a.min()         # Array-wise minimum
b.max(axis=0)   # Maximum value of an array row
b.cumsum(axis=1)# Cumulative sum of the elements
a.mean()        # Mean
np.median(a)    # Median
np.std(b)       # Standard deviation
```

**Array Manipulation:**
```python
b.reshape(3, 2) # Reshape without changing data
np.append(a, b) # Append items
np.insert(a, 1, 5) # Insert items
np.delete(a, [1])  # Delete items
np.concatenate((a, d), axis=0) # Concatenate arrays
```

---

## 2. Matplotlib (Pyplot)
*Comprehensive library for creating static, animated, and interactive visualizations.*

**Import:**
```python
import matplotlib.pyplot as plt
```

**Basic Plotting:**
```python
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)               # Create a line plot
plt.show()                   # Display the plot
```

**Figure and Axes (Object-Oriented API):**
```python
fig, ax = plt.subplots()     # Create a figure and an axes
ax.plot(x, y, label='Sine')  # Plot some data on the axes
ax.set_xlabel('X Label')     # Set x-axis label
ax.set_ylabel('Y Label')     # Set y-axis label
ax.set_title('My Plot')      # Set title
ax.legend()                  # Show legend
```

**Types of Plots:**
```python
plt.scatter(x, y)            # Scatter plot
plt.bar(x, y)                # Bar chart
plt.hist(y, bins=20)         # Histogram
plt.boxplot(y)               # Box plot
plt.imshow(image_array)      # Show image/heatmap
```

**Customization:**
```python
plt.plot(x, y, color='red', linestyle='--', linewidth=2, marker='o')
plt.xlim(0, 5)               # Set x limits
plt.ylim(-1, 1)              # Set y limits
plt.grid(True)               # Show grid
```

**Saving Plots:**
```python
plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')
```

---

## 3. SciPy (Scientific Python)
*Library for advanced mathematical, scientific, and engineering functions (builds on NumPy).*

**Import (usually import specific submodules):**
```python
import scipy as sp
from scipy import optimize, integrate, interpolate, signal, linalg, stats
```

**Optimization (`scipy.optimize`):**
```python
from scipy.optimize import minimize, curve_fit

# Minimize a function
def rosen(x): return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)
res = minimize(rosen, [1.3, 0.7, 0.8, 1.9, 1.2])

# Curve fitting
def func(x, a, b, c): return a * np.exp(-b * x) + c
popt, pcov = curve_fit(func, xdata, ydata)
```

**Integration (`scipy.integrate`):**
```python
from scipy.integrate import quad, odeint

# Definite integral
res, err = quad(lambda x: np.exp(-x**2), 0, np.inf)

# Ordinary Differential Equations (ODEs)
def model(y, t): return -k * y
y = odeint(model, y0, t)
```

**Interpolation (`scipy.interpolate`):**
```python
from scipy.interpolate import interp1d

f = interp1d(x, y, kind='cubic')
y_new = f(x_new)
```

**Linear Algebra (`scipy.linalg`):**
*More advanced than `numpy.linalg`.*
```python
from scipy import linalg

A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
x = linalg.solve(A, b)       # Solve linear systems (Ax = b)
det = linalg.det(A)          # Determinant
inv = linalg.inv(A)          # Inverse
eigvals, eigvecs = linalg.eig(A) # Eigenvalues and eigenvectors
```

**Statistics (`scipy.stats`):**
```python
from scipy import stats

norm_dist = stats.norm(loc=0, scale=1) # Normal distribution
norm_dist.pdf(x)             # Probability density function
norm_dist.cdf(x)             # Cumulative distribution function
stats.ttest_ind(a, b)        # T-test for independent samples
```
