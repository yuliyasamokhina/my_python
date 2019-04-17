value = input("Введите атомный номер элемента:")
if value:
    AN = int(value)
    if AN == 3:
        print("Литий")
    elif AN == 25:
        print("Марганец")
    elif AN == 17:
        print("Хлор")
    elif AN == 80:
        print("Ртуть")
    else:
        print("Что это?!")
else:
    print("Введите атомный номер!")
