def adunare():
    a = int(input("Introduceti a: "))
    b = int(input("Introduceti b: "))
    print("a+b= ", a+b)

def scadere():
    a=int(input("Introduceti a: "))
    b=int(input("Introduceti b: "))
    print("a-b= ", a-b)

def inmultire():
    a = int(input("Introduceti a: "))
    b = int(input("Introduceti b: "))
    print("a*b= ", a * b)

def impartire():
    a = int(input("Introduceti a: "))
    b = int(input("Introduceti b: "))
    print("a/b= ", a / b)

def sumacifre2():
    nr=int(input("Introduceti un numar de 2 cifre: "))
    d1=nr%10
    d2=nr//10
    print(d1+d2)


if __name__ == "__main__":
    adunare()
    #scadere()
    #inmultire()
    #impartire()
    #sumacifre2()