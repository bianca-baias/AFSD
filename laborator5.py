def citire_lista_cu_for():
    l= list()
    size= int(input("Dimensiunea listei: "))
    for i in range (size):
        l.append(int(input("Elementul " + str(i) + ' ')))
        i=i+1
    return l

def citire_lista_cu_while():
    l= list()
    size= int(input("Dimensiunea listei: "))
    i=0
    while i < size:
        l.append(int(input("Elementul " + str(i) + ' ')))
        i=i+1
    return l

def minim_maxim_lista(lista):
    minim = lista[0]
    maxim = lista[0]
    for element in lista:
        if element <= minim:
            minim = element
        elif element > maxim:
            maxim = element
    return[minim, maxim]


def modificare_lista(lista, valoare, pas):
    if pas <= len(lista):
        for i in range(len(lista)):
            if (i+1) % pas == 0:
                lista[i] += valoare
    return lista

def suma(n):
    suma=0
    for i in range(n+1):
        suma +=i
    return suma

def suma_while(n):
    suma=0
    i=1
    while i<= n:
        suma +=i
        i+=1
    return suma

def produs(n):
    produs=1
    for i in range(1, n+1):
        produs = produs * i
    return produs
def produs_while(n):
    produs=1
    i=1
    while i<=n:
        produs=produs*i
        i+=1
    return produs


if __name__ == "__main__":
    numar= int(input("Introduceti un numar: "))
    print(produs_while(numar))
    #print(produs(numar))
    #print(suma_while(numar))
    #l1=citire_lista_cu_for()
    #l2=citire_lista_cu_while()
    #print(modificare_lista(l1, 2, 5))
    #min_max=minim_maxim_lista(l1)
    #print("Minimul este: " ,min_max[0] , " Iar maximul este: " , min_max[1])