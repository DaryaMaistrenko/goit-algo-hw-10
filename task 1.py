from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

# Створення моделі
model = LpProblem("Maximize_Production", LpMaximize)

# Змінні: кількість "Лимонаду" (L) і "Фруктового соку" (F)
L = LpVariable("Lemonade", lowBound=0, cat="Integer")
F = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Цільова функція: максимізувати загальну кількість вироблених продуктів
model += L + F, "Total_Production"

# Обмеження на ресурси
model += 2 * L + 1 * F <= 100, "Water_Constraint"
model += 1 * L <= 50, "Sugar_Constraint"
model += 1 * L <= 30, "Lemon_Juice_Constraint"
model += 2 * F <= 40, "Fruit_Puree_Constraint"

# Розв'язання задачі
model.solve()

# Виведення результатів
lemonade_count = L.varValue
fruit_juice_count = F.varValue
total_production = value(model.objective)

print(f"Optimal production of Lemonade: {lemonade_count}")
print(f"Optimal production of Fruit Juice: {fruit_juice_count}")
print(f"Total Production: {total_production}")
