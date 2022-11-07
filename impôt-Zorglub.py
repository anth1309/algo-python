


sexe,age=input("Bonjour, êtes vous un homme ou une femme (h/f) ? "),int(input("Quel âge avez vous ?"))
sexe=sexe.upper()
if (sexe=="H" and age>=20) or (sexe=="F" and (age>=18 and age<=35)):
    print("Nous avons le plaisir de vous informer que vous êtes redevable de l'impôt")
else :
    print("Désolé, vous ne participerez pas à l effort national")
    