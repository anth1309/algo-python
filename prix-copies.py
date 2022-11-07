nombre=""
prix=""

nombre=int(input ("Combien voulez vous faire de photocopies ? ") )

if nombre <=10 :
    print (f"vous devrez payez {nombre*0.10} €,pour {nombre} copies ")
elif nombre <= 30 :
        print (f"vous devrez payez {1+(nombre-10)*0.09} €,pour {nombre} copies ")
else :
        print (f"vous devrez payez {2.8+(nombre-30)*0.08} €,pour {nombre} copies ")
    