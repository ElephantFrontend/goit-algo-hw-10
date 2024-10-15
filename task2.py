# Імпортуємо потрібні ліби.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначимо функцію для інтегрування.
def f(x):
    return np.sin(x) + 0.5

# Параметри інтегрування.
a, b = 0, np.pi  # межі інтеграції.

# Метод Монте-Карло для обчислення інтегралу.
N = 10000  # кількість випадкових точок.
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, 1.5, N)

# Обчислення кількості точок під кривою.
below_curve = y_random < f(x_random)
monte_carlo_integral = ((b - a) * 1.5) * np.mean(below_curve)

# Точне значення інтегралу за допомогою SciPy quad.
exact_integral, _ = quad(f, a, b)

# Побудова графіка.
x = np.linspace(a, b, 500)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', label="f(x) = sin(x) + 0.5")
plt.fill_between(x, y, color="gray", alpha=0.3, label="Інтегральна область")
plt.scatter(x_random, y_random, color="red", s=1, alpha=0.1, label="Випадкові точки")
plt.title("Інтеграція методом Монте-Карло")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

# Виведення результатів.
plt.show()
print("Значення інтегралу методом Монте-Карло:", monte_carlo_integral)
print("Точне значення інтегралу:", exact_integral)
print("Абсолютна різниця:", abs(monte_carlo_integral - exact_integral))


# Висновок
# Метод Монте-Карло є надійним для наближених обчислень значень інтегралів і може 
# бути використаний у випадках, коли інші методи обчислення є складними або недоступними. 
# Незважаючи на те, що він не є найточнішим методом для простих функцій, у деяких 
# ситуаціях, таких як складні багатовимірні інтеграли, він є одним із найкращих виборів.