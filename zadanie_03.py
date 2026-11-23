n = int(input("wpisz liczbę całkowitą: "))

for n in range(1, n + 1):
    if (n % 2 == 0): 
        print(n)
        n = n - 2
    
