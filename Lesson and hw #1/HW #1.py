import math

# 1 Арифметичні операції: Написати програму, яка зчитує два числа та виводить їхню суму, різницю, добуток та частку.

varieble_1 = 15
varieble_2 = 10
varieble_3 = 5

print(varieble_1 + varieble_2)
print(varieble_1 * varieble_2)
print(varieble_1 / varieble_2)
print(varieble_1 - varieble_2)

result = varieble_2 + varieble_1
print(result)
result = varieble_2 * varieble_1
print(result)
result = varieble_1 / varieble_2
print(result)
result = varieble_1 - varieble_2
print(result)


# 2 Залишок від ділення: Користувач вводить два числа. Вивести залишок від ділення першого числа на друге.
result = varieble_1 % varieble_3

print(result)

# 3 Цілочисельне ділення: Користувач вводить два числа. Вивести, скільки разів перше число ділиться на друге без залишку.

result = varieble_1 // varieble_3
print(result)

# 4 Перетворення стрічки у число: Користувач вводить рядок, який складається з цифр. Програма повинна перетворити його на число та вивести.

sample_text = "hello word"
print(sample_text)
print(type(sample_text))

sample_text_1 = "5"
sample_text_2 = "4"

print(sample_text_1)
print(type(sample_text_1))
print((sample_text_1 + sample_text_2))

# 5 Стрічкова конкатенація + математика:
# Користувач вводить два числа. Програма повинна вивести два прінти: перший — їхню суму,
# другий об'єднати їх. Якщо в нас числа 5 та 4, то результат повинен бути 9 та 54.

sample_text_1_int = int(sample_text_1)
sample_text_2_int = int(sample_text_2)
result = (sample_text_2_int + sample_text_1_int)
print(result)

# 6 Вік користувача:
# Запитати у користувача його рік народження, ім'я та який зараз рік (три змінні)
# та вивести на екран два прінти: ім'я та скільки років користувачу.

age = int(input("How old are you ?"))
print(age)
print(type(age))

name = input("Whats your name ?")
print(name)
print(type(name))


# 7 Перевод з цельсія в фаренгейт:
# Напишіть програму, яка запитує в користувача кількість градусів в цельсіях і повертає в фаренгейтах.

c = int(input("Enter degrees Celsius"))
f = ((c * 9) / 5) + 32
print(f"{c} degrees Celsius equals {f} degrees Fahrenheit")

# 8 Перевод з фаренгейта в цельсій:
# Напишіть програму, яка запитує в користувача кількість градусів в фаренгейтах і повертає в цельсіях.
# Вам може здатися, що ця задача така ж, як попередня, але будьте уважні і перевірте результат вручну.

f = int(input("Enter degrees Fahrenheit"))
c = ((c * 9) / 5) + 32
print(f"{c} degrees Fahrenheit equals {f} degrees Celsius")

# 10 Школярі та яблука
# n школярів ділять k яблук порівну, недільний залишок залишається в кошику.
# Скільки яблук дістанеться кожному школярові та скільки залишиться в кошику?
# Програма отримує на вхід числа n і k - цілі, додатні, не перевищують 10000.

n = int(input("Apples:"))
k = int(input("Pupils:"))
print(n % k, n // k)

# 12 Циферблад
# Запитайте в користувача скільки хвилин пройшло з початку доби.
# Визначте, скільки годин і хвилин покаже електронний годинник в цей момент і поверніть йому результат (формататування тексту при ввиводі не важливе).
# приклад для перевірки програми 1
# користувач ввів:150
# користувач отримує: 2, 30
# приклад для перевірки програми 2
# користувач ввів:1441
# користувач отримує: 0, 1

n = int(input("Enter data"))
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)

# 9 Теорема Піфагора:
# Запитайте у користувача довжини катетів та виведіть на екран довжину гіпотенузи.
# Трикутник рівнобедрений. Що б взвести в степінь ставимо два рази множення
# два в степені три буде так 2**3, квадратний корінь з двух буде 2**(1/2)

a = input("a = ")
b = input("b = ")

a = float(a)
b = float(b)

area = (a * b) / 2

c = math.sqrt(a**2 + b**2)

perimeter = a + b + c

print("Area:", area)
print("Perimeter:", perimeter)

# 11 Магазин канцелярських товарів
# Одного разу, відвідавши магазин канцелярських товарів, Вася купив X олівців, Y ручок та Z фломастерів. Відомо,
# що ціна ручки на 2 гривні більше ціни олівця та на 7 гривень менше ціни фломастера. Також відомо,
# що вартість олівця становить 3 гривні. Потрібно визначити загальну вартість покупки.
# Вхідні дані
# просимо користувача ввести три змінні
# кожне з яких не перевищує 109.
# Вихідні дані
# виведіть одне ціле число – вартість покупки в гривнях.
# приклад для перевірки програми 1
# ввів: 1 1 1
# отримав: 20

X = int(input())
Y = int(input())
Z = int(input())
A = 3
B = 5
C = 12
print(X*A+Y*B+Z*C)