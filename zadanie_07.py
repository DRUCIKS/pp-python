n = int(input("wpisz liczbę studentów: "))
suma = 0

for _ in range(n):
    while True:
        wynik = int(input("wprowadź wynik studenta: "))
        if wynik < 0 or wynik > 100:
            print("Niepoprawny wynik")
        else:
            suma += wynik
            break

print(f"Suma: {suma}")


