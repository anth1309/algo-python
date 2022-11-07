age=0
anneedepermis=0
tarif=0

age=int(input("Quel est votre âge ? "))
anneedepermis=int(input("Depuis combien de temps avez vous le permis ? "))
#anneechezassurreur=int(input("Depuis combien d année(s) êtes vous assuré chez nous ? "))
accident=int(input("Combien avez vous eu d'accident(s) ? "))

A= (age>=25)
B=(anneedepermis>=2)
#C=(anneechezassurreur>5)

rouge=4
orange=3
vert=2
bleu=1





if not A and not B and accident==0:
    print(f"Vous avez droit au tarif rouge  ")
    
elif (not A and B) or (A and not B):
    if accident==0 :
        print(f"Vous avez le droit au tarif orange ")
    elif int(accident)==1 :
        print("Vous avez droit au tarif rouge")
    else :
        print("Désolé nous ne pouvons pas vous assurez")

elif  A and B:
    if accident==0 :
        print(f"Vous avez le droit au tarif vert ")
    elif int(accident)<=1 :
        print("Vous avez droit au tarif orange")
    elif int(accident)<=2 :
        print("Vous avez droit au tarif rouge")
    else :
        print("Désolé nous ne pouvons pas vous assurez")

else :
    print("Désolé nous ne pouvons pas vous assurez")





#elif C :
 #   tarif=int(tarif)-1


#else :
        #print("Désolé nous ne pouvons pas vous assuré"):