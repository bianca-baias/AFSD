#Sa se def o functie care primeste ca parametru un sir de caractere si tipareste ca rezultat sirul in urmatorul format:
#din sirul original se pastreaza doua treimi, dupa care litera aflata la pozitia 2/3 se inlocuieste cu ansamblul format din
#1 litera marita si cifra doi, iar restul sirului se pastreaza cum este el.

def format_string(sir):
    pozitia_dorita = (len(sir)*2)//3
    litera = sir[pozitia_dorita]
    print(sir[: pozitia_dorita] + "1" + litera.upper() + "2" + sir[pozitia_dorita + 1:])


if __name__ == "__main__":
    sir = input("Introduceti sirul de caractere: ")
    format_string(sir)
