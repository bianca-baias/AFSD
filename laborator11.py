#Sirul lui Fibonacci

def fibonacci(valoare):
    n1=0
    n2=1
    sir_fibonacci=[]
    sir_fibonacci.append(n1)
    sir_fibonacci.append(n2)
    while n2 < valoare:
        temp=n1
        n1=n2
        n2= temp + n1
        sir_fibonacci.append(n2)
    return sir_fibonacci

#generare CNP

def cnp(gen, an, luna, zi, judet, numar): #exemplu: 'M', 1997, 12, 16, 24, 507
    c1=''
    c23 = ''
    c45= ''
    c67=''
    c89='' #judet
    c1012='' #nr ordine
    c13='' #control

    if gen == 'M':
        if an < 2000:
            c1='1'
            c23=str(an%100)
        elif an >= 2000:
            c1= '5'
            c23=str(an%100)
    elif gen == 'F':
        if an < 2000:
            c1='2'
            c23=str(an%100)
        elif an >= 2000:
            c1= '6'
            c23=str(an%100)
    c45=str(luna)
    c67=str(zi)
    c89=str(judet)
    c1012=str(numar)
    sir_verificare='279146358279'
    sir_cnp= c1 + c23 + c45 + c67 + c89 + c1012
    suma = 0
    for i in range(len(sir_verificare)):
        suma += int(sir_verificare[i]+sir_cnp[i])
    if suma%11 == 10:
        c13='1'
    else:
        c13=str(suma%11)
    sir_cnp = sir_cnp + c13

    return sir_cnp



if __name__ == "__main__":
    #print(fibonacci(1000))
    print(cnp('F', 1997, 12, 16, 24, 507))