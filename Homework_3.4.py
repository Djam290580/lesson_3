# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# ----------Вариант 1---------------------------------------------------------------
def my_func(x, y):
    return x ** y

print(my_func(4, -2))
#---------------------------------
# def my_func(x, y):
#     print(pow(x, y))
#
# my_func(4, -2)
#--------------------------------
# -------------------------------------------Вариант 2----------------------------------------------------------------
def my_func(x, y):
    i = 0; b = 0
    while i <= y:
        b = x * x
        i += 1
    print(b)

my_func(2, 3)





