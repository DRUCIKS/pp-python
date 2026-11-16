
n = int(input("Podaj liczbę całkowitą n: "))
if n <= 0:
    print("Błąd")

for i in range(n):
    if i == 0:
        wynik = 0
    else:
        wynik = 2 ** i
    print(f"Python {wynik}")
