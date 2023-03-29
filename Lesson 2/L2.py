import random

# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

"""
print("Задание 2.1")
pers_health = None
while input("enter here: "):
    pers_health = random.randint(-5, 5)
    print(f"{pers_health} --> False") if pers_health <= 0 else print(f"{pers_health} --> True")
"""
# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным.
# Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
"""
print("\nЗадание 2.2\n")
print("Нечетное") if int(input()) % 2 else print("Четное")
"""

# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и
# не являются столетиями (500, 600).
# Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)

"""
print("\nЗадание 2.3\n")
year = int(input())
if year % 4 or year in range(100, 900, 100):
    print("не високосный ", year % 4)
else:
    print("високосный ", year % 4)
"""
# Задание 2.4
# Напишите программу,
# которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()
"""
print("\nЗадание 2.4\n")
text, rep = map(str, input().split())
print(text, rep)
# вар 1
for i in range(int(rep)):
    print(text, sep=('\n'))
# вар 2
[[print(f"{text}")] for i in range(int(rep))]
"""

# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат
# в формате: {num1} {operator) {num2) = {result}

print("\nЗадание 2.5\n")
a, b, op = map(str, input("введите два числа и оператор через пробелы в строчку: ").split())

if op == "+":
    result = int(a) + int(b)
if op == "-":
    result = int(a) - int(b)
if op == "/":
    result = int(a) / int(b)
if op == "*":
    result = int(a) * int(b)

print(f"{a} {op} {b} = {result}")


"""
if num2 == 0 and operator == '/':
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")
else:
    result = eval(f'{num1} {operator} {num2}')
    print(f'{num1} {operator} {num2} = {result}')
"""

