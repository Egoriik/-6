from sqlalchemy.sql.operators import truediv


def one():
    num = int(input("Введите число: "))
    if num % 3 == 0:
        print("Да, число делится на 3")
    else:
        print("Нет, число не делится на 3")

def two():
    num = int(input("Введите число: "))
    res = 100/num
    try:
        print(f"100 : {num} = {res}")
    except ValueError:
        print("Вводите значения цифрами!")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")

def three():
    print("Пожалуйста, вводите все значения цифрами!")
    day = int(input("Введите день:"))
    month = int(input("Введите месяц: "))
    year = input("Введите год: ")
    if not(1<= day <= 31):
        print("День должен быть в промежутке 1-31")
        if not(1<=month<=12):
            print("Месяц должен быть в промежутке 1-12")
    else:
        if day*month == int(year[:2]):
            print("Дата является магической")
        else:
            print("дата не является магической")

def four():
    num = input("Введите номер своего билета: ")
    if len(num) != 6:
        print("Номера всегда четной длиныЙ")
    else:
        srez = int(len(num)) // 2
        sum1 = sum(map(int, num[srez:]))
        sum2 = sum(map(int, num[:srez]))
        print(sum1)
        print(sum2)
        if sum1 == sum2:
            print("Ваш билет счастливый!")
        else:
            print("Ваш билет не счастливый...")



enter = int(input("Какое задание хотите выполнить:\n"
         "1 - Проверка деления вводимого числа на 3\n"
         "2 - Деление 100 на вводимое число \n"
         "3 - Магическая дата \n"
         "4 - Счастливый билет \n"
         "Выберите задание: "))
print(f"\nВыполняется функция {enter}")
if enter == 1:
    one()
if enter == 2:
    two()
if enter == 3:
    three()
if enter == 4:
    four()