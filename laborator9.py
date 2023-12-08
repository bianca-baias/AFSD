def citire_matrice(l, c):
    matrice = []
    for i in range(l):
        matrice.append([])
        for j in range(c):
            matrice[i].append(int(input(f"Linie {i}, coloana {j}: ")))
    return matrice


if __name__ == "__main__":
    l=3
    c=3
    print(citire_matrice(l, c))
