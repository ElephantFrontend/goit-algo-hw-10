# Імпортуємо потрібну лібу.
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

# Створюємо об'єкт проблеми максимізації.
model = LpProblem(name="maximize-production", sense=LpMaximize)

# Створюємо змінні для кількості виробництва Лимонаду і Фруктового соку.
lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Додаємо цільову функцію: максимізувати кількість вироблених продуктів.
model += lemonade + fruit_juice, "Total Products"

# Додаємо обмеження по ресурсам.
model += (2 * lemonade + 1 * fruit_juice <= 100), "Water Constraint"     # Обмеження на воду.
model += (1 * lemonade <= 50), "Sugar Constraint"                        # Обмеження на цукор.
model += (1 * lemonade <= 30), "Lemon Juice Constraint"                  # Обмеження на лимонний сік.
model += (2 * fruit_juice <= 40), "Fruit Puree Constraint"               # Обмеження на фруктове пюре.

# Розв'язуємо модель.
model.solve()

# Отримуємо результати.
lemonade_count = lemonade.varValue
fruit_juice_count = fruit_juice.varValue
total_products = value(model.objective)

print(f"Лимонад: {lemonade_count}, Фруктовий сік: {fruit_juice_count}, Всього продуктів: {total_products}")
