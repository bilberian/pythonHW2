# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N

N = int(input('Введите число N: '))
exp = 0
res = 1
while res < N:
    res = 2 ** exp
    exp += 1
    if res > N: 
        break
    print(res, end=' ')
