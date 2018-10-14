rzeczy = ["doniczka", "kwiatek", "ziemia", "woda"]

print(rzeczy[1])
print(rzeczy[1:3])
print(len(rzeczy))

rzeczy[2] = "konewka"
print(rzeczy)

#krotka
krotka = (1, 2, 700)
x, y, *reszta = krotka
print(x)
print(y)
print(*reszta)