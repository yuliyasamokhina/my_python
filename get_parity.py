def parity(x):
    return x%2
x = int(input('Введите число: '))
if parity(x) == 0:
    print('Число является четным')
else:
    print('Число не является четным')
