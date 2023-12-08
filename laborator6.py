#sa se def o functie care primeste ca param un nr intreg, si return true sau false daca nr e par sau immpar
# o fct care folosind instr while va citi niste nr intregi de la tastatura, si va returna nr de numere pare, respectiv impare

#iesirea din ciclul while se face cand nr citit de la tastatura este 0

#cautarea secventiala a unei valori intr-o lista folosind o fct care intoarce indexul elementului, daca e gasita valoarea, si -1 in caz contrar
def par_impar(nr):
    if nr % 2 == 0:
        return True
    else:
        return False

def numar_de_numere():
    nr = int(input("Introduceti un nr: "))
    par=0
    impar=0
    while nr != 0:
        if par_impar(nr):
            par += 1
        else:
            impar += 1
        nr = int(input("Introduceti un nr: "))
    print("Numere pare: ", par)
    print("Numere impare: ", impar)
    return par, impar

def cautare_secventiala(lista, element):
    if element in lista:
        return lista.index(element)
    else:
        return -1

if __name__ == "__main__":
    x=numar_de_numere()
    print(type(x))
    lista=[1,5,7,11,0,3,7]
    element=7
    print(cautare_secventiala(lista, element))