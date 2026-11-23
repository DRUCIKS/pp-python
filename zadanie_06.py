
suma = 0
liczba_wartosci = 0

while True:
    a = int(input())
    if a == 0:
        break
    suma += a
    liczba_wartosci += 1

print("suma" + "" + ":" + str(suma))
print("Liczba wartości" + "" + ":" + str(liczba_wartosci))
