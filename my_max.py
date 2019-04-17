def max(x,y):
    return x > y
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
if max(x,y) == True:
    print ('Максимальное число:',x)
else: 
    print ('Максимальное число:',y)

