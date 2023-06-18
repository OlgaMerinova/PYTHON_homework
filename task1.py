#Нарисовать в консоли ёлку спросив у пользователя количество рядов.


rows = int(input("Введите количество рядов "))
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
