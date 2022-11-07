candidata,candidatb,candidatc,candidatd=float(input("Veuillez rentrer le score du candidat A :")),float(input("candidat B :")),float(input("candidat C :")),float(input("candidat D :"))
comparaison1=(candidata>50)
comparaison2=(candidatb>50 or candidatc>50 or candidatd>50)
comparaison3=( candidatb<candidata and candidatc<candidata and candidatd<candidata)
comparaison4=(candidata<12.5)



if comparaison1 :
    print ("Félicitation le candidata est élu")
elif comparaison2 or comparaison4:
    print("Vous avez perdu appellez un ami pour 'pantoufler'")
elif   comparaison3 and not comparaison1:
    print("Ouf c été juste mais vous allez au deuxieme tour,vous êtes en tête")
else :
    print("Vous allez au second tour mais ca va être trés compliqué")