import math
def cautare_binara(lista, valoare):
    lista.sort()
    while len(lista)>1:
        l1=lista[:len(lista)//2]
        l2=lista[len(lista)//2:]
        if valoare >= l1[0] and valoare<= l1[-1]:
            lista=l1
        else:
            if valoare >= l2[0] and valoare<= l2[-1]:
                lista=l2
            else:
                lista=[]
    if len(lista)==0:
        return None
    else:
        return lista[0]

def functia_gr_2(a, b, c):
    delta=b**2 - 4*a*c
    if delta>0:
        x1=(-b + math.sqrt(delta))/(2*a)
        x2=(-b - math.sqrt(delta))/(2*a)
    elif delta==0:
        x1=x2=(-b)/(2*a)
    elif delta<0:
        x1=x2=None
    return x1, x2

def conversie2_10(numar):
    n = len(numar) - 1
    baza_10 = 0
    for el in numar:
        baza_10 = baza_10 + int(el) * (2 ** n)
        n = n - 1
    return (baza_10)

def conversie10_2(numar):
    sir=''
    while numar > 1:
        r=numar % 2
        c=numar // 2
        numar=c
        sir= sir + str(r)
    sir= sir + str(numar)
    return sir[-1::-1]

if __name__ == "__main__":
    lista = [1, 7, 5, 10, 8, 1, 99]
    valoare = 5
    numar='1001001'
    #print(cautare_binara(lista, valoare))
    #print(functia_gr_2(1,2,1))
    #print(conversie2_10(numar))
    #print(conversie10_2(56))
