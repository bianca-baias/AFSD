
def cautare_secventiala(lista, valoare):
    for i in range(len(lista)):
        if lista[i] == valoare:
            return valoare
    return None

def cautare_binara(lista, valoare):
    lista.sort()
    l1=lista[:len(lista)//2]
    l2=lista[len(lista)//2 :]
    if (valoare >= l1[0]) and (valoare <= l1[len(l1) - 1]):
        return cautare_secventiala(l1, valoare)
    if (valoare >= l2[0]) and (valoare <= l2[len(l2) -1]):
        return cautare_secventiala(l2, valoare)
    return None

def bubble_sort(lista):
    flag=1
    z=0
    #for i in  range(len(lista)):
    while flag==1:
        flag=0
        for j in range(len(lista)-z-1):
            if lista[j]>lista[j+1]:
                x=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=x
                flag=1
        z += 1
    return lista

def conversie2_10(numar):
    n=len(numar)-1
    baza_10=0
    for i in range(len(numar)):
        baza_10=baza_10 + int(numar[i])*(2**n)
        n=n-1
    return(baza_10)

if __name__ == "__main__":
    lista=[1, 7, 5, 10, 8, 1, 99]
    valoare= 1
    numar='1001001'
    print(conversie2_10(numar))
    #print(bubble_sort(lista))
    #print(cautare_binara(lista, valoare))
    #print(cautare_secventiala(lista, valoare))
