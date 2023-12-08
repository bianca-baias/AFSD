def reverse_parameter(parameter):
    print(parameter[::-1])

def verificare_invers(parameter):
    if parameter == parameter[::-1]:
        print("Sirul este palindrom.")
    else:
        print("Sirul nu este palindrom.")

def slice_parameter(parameter):
    j1 = parameter[:len(parameter)//2]
    j2 = parameter[len(parameter)//2 :]
    print(j1)
    print(j2)

def nr_vocale(sir):
    parameter.lower()
    a = sir.count('a')
    e = sir.count('e')
    i = sir.count('i')
    o = sir.count('o')
    u = sir.count('u')
    print(a+e+i+o+u)


if __name__ == "__main__":
    parameter = input("Introduceti un sir: ")
    nr_vocale(parameter)
    #slice_parameter((parameter))
    #verificare_invers(parameter)
    #reverse_parameter(parameter)
