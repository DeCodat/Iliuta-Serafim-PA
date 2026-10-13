with open('numere.txt', 'r') as fisier:
    # .read().split() extrage toate cuvintele separate de spații sau rânduri noi
    # Convertim fiecare element în 'int' (sau 'float' dacă ai zecimale) și facem suma
    suma = sum(int(x) for x in fisier.read().split())

print(f"Suma este: {suma}")