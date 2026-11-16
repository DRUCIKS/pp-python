a = int(input("Wprowadź liczbę punktów uzyskanych przez studenta: "))

if a >= 10:
    print("Zaliczone")
else:
    print("Niezaliczone")

if a<= 10:
    print("Brakujące punkty: ")
    print(10 - a)