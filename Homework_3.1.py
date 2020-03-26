# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func_1(a_1 = int(input("Введите число ")), a_2 = int(input("Введите число "))):
    try:
        a_3 = 0
        a_3 = int(a_1 / a_2)
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "На ноль делить нельзя!!! Попробуйте еще раз!"
    return a_3

print(my_func_1())

#----------------------------------

# def my_func_2(*args):
#     try:
#         a_1 = int(input("Введите число "))
#         a_2 = int(input("Введите число "))
#         a_3 = a_1 / a_2
#     except ValueError:
#         return 'Value error'
#     except ZeroDivisionError:
#         return "На ноль делить нельзя!!! Попробуйте еще раз!"
#     return a_3
#
# print(my_func_2())


