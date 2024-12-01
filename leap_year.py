annee = int(input("Entrez une annee : "))

if annee % 4 == 0:
    if annee % 100 == 0:
        if annee % 400 == 0:
            print(annee, "est une annee bissextile.")
        else:
            print(annee, "n'est pas une anne2022e bissextile.")
    else:
        print(annee, "est une annee bissextile.") 

else:
    print(annee, "n'est pas une annee bissextile.")