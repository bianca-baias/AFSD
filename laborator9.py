def citire_matrice():
    l=int(input("Introduceti nr de linii: "))
    c=int(input("Introduceti nr de coloane: "))
    matrice = []
    for i in range(l):
        matrice.append([])
        for j in range(c):
            matrice[i].append(int(input(f"Linie {i}, coloana {j}: ")))
    return matrice

def citire_matrice2(l,c):
    matr=[[0 for _ in range(c)] for _ in range(l)]
    for i in range(l):
        for j in range(c):
            matr[i][j] = int(input(f"Elementul {i}, {j} = "))
    return matr


def afisare_matrice(m): #m- matricea
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{i}, {j}= {m[i][j]}")


def diag_secundara(m):
    x=len(m)-1
    for i in range(len(m)-1):
        for j in range(x):
            m[i][j]= m[i][j]**2
        x-=1
    return m


#sa se def o fct care primeste ca parametrii un sir si un nr intreg mai mic ca len(sir)
#si reintoarce sirul cu primele x litere mici
def micsorare(sir, x):
    return sir[:x].lower() + sir[x:]


if __name__ == "__main__":
    #m=citire_matrice2(3,3)
    print(micsorare("PYTHON", 2))
