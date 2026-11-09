# Wczytanie liczby całkowitej
liczba = int(input("wpisz liczbę całkowitą"))

# Pierwszy niezależny warunek - sprawdzenie czy dodatnia
if liczba > 0:
    print("Dodatnia")

# Drugi niezależny warunek - sprawdzenie parzystości
if liczba % 2 == 0:
    print("Parzysta")