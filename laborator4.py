def min_max(lista):
    lista.sort()
    print("Minimul este: ", lista[0], "- Maximul este: ", lista[len(lista)-1], " sau ", lista[-1])

def prod_min_max(lista):
    lista.sort()
    print("Produsul dintre minim si maxim este: ", lista[0] * lista[-1])

if __name__ == "__main__":
    min_max([6, 100, 2, 3, 1, 45])
    prod_min_max([6, 100, 2, 3, 1, 45])