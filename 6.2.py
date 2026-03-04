def f(num):
    if num == 0:
        print("На ноль делить нельзя!")
    else:
        res = 100/num
        print(f"100 : {num} = {res}")

num = int(input("Введите число: "))
f(num)