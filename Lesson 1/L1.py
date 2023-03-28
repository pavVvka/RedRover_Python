import random

# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
print("Задание 2.1")
pers_health = None
while input("enter here: "):
    pers_health = random.randint(-5, 5)
    print(f"{pers_health} --> False") if pers_health <= 0 else print(f"{pers_health} --> True")
