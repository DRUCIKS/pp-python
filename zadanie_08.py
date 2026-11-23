n = int(input())

poprawne = 0

for liczba in range(1, n + 1):
    print(f"Podaj kwadrat liczby {liczba}")
    
    próba = 1
    zgadnieto = False
    kwadrat = liczba * liczba
    
    while próba <= 3 and not zgadnieto:
        odpowiedz = int(input())
        
        if odpowiedz == kwadrat:
            print("Poprawna odpowiedź")
            zgadnieto = True
            poprawne += 1
        else:
            print("Błędna odpowiedź")
            próba += 1

print(f"Poprawnie rozwiązane: {poprawne}")



