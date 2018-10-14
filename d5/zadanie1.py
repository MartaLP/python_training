# stworzyć funkcję która po otrzymaniu dwóch liczb
# będzie drukować niepełną piramidę. Dla liczba 5 i 7:
# #########
# ###########
# #############


def piramida (a, b):
    for i in range(a-1, b):
        print(' ' * (b - i - 1) + '*' * (2 * i + 1))

piramida(5, 7)

