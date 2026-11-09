# Wczytanie danych (domyślnie input() pobiera wszystko jako tekst)
tekst1 = input("Wprowadź pierwszą liczbę całkowitą")
tekst2 = input("Wprowadź drugą liczbę która posiada przecinek")

# 1. Wynik porównania wczytanych tekstów
wynik_teksty = tekst1 == tekst2
print("Czy są sobie równe ?", wynik_teksty)

# Konwersja na odpowiednie typy liczbowe
liczba_calkowita = int(tekst1)
liczba_zmiennoprzecinkowa = float(tekst2)

# 2. Wynik porównania wartości po konwersji
wynik_wartosci = liczba_calkowita == liczba_zmiennoprzecinkowa
print("Jakie mają wartości", wynik_wartosci)

# 3. Sprawdzenie, czy pierwsza jest większa od drugiej
czy_wieksza = liczba_calkowita > liczba_zmiennoprzecinkowa
print("Czy pierwsza jest większa od drugiej (>):", czy_wieksza)