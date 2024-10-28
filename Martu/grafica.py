import numpy as np
import matplotlib.pyplot as plt

# Valores de a y b para la hipérbola
a = 3
b = 2

# Rango de valores para x y y
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)

# Ecuación de la hipérbola
Z = X**2 / a**2 - Y**2 / b**2 - 1

# Configuración de la gráfica
plt.figure(figsize=(8, 8))
plt.contour(X, Y, Z, levels=[0], colors='blue')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.scatter([a, -a], [0, 0], color='red', zorder=5, label="Vértices (3, 0) y (-3, 0)")
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title("Hipérbola con eje transversal horizontal")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()
