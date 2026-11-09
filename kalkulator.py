# Wczytanie danych w trzech osobnych liniach
liczba1 = float(input("wprowadź liczbę"))
operator = input("wprowadź operatora")
liczba2 = float(input("wprowadź kolejną liczbę"))

# Osobne instrukcje if dla każdego działania
if operator == '+':
    print(liczba1 + liczba2)

if operator == '-':
    print(liczba1 - liczba2)

if operator == '*':
    print(liczba1 * liczba2)

if operator == '/':
    # Zagnieżdżone instrukcje if do obsługi dzielenia przez zero
    if liczba2 != 0:
        print(liczba1 / liczba2)
    if liczba2 == 0:
        print("Nie można dzielić przez zero")