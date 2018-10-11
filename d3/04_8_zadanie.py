# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

#print("Podaj 3 boki trojkata:")
#a = float(input("a:"))
#b = float(input("b:"))
#c = float(input("c:"))

a = 3
b = 2
c = 1.2

if a + b > c and a + c > b and b + c > a:
    print("Uda się narysować trojkat.")
    if a == b and b == c:
        print("Trójkąt równoboczny.")
    elif ((a == b and b != c ) or (a == c and c != b) or (b == c and c != a)):
        print("Trójkąt równoramienny.")
    else:
        print("Trójkąt różnoboczny")
else:
    print("Nie uda się narysować.")