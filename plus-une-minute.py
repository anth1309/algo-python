h=""
m=""

h=input ("entrez l heure : ") 
m=input ('entrez les minutes : ')
h=int(h)
m=int(m)
m=m+1
if m!=60 :
    print (f"Dans une minute il sera {h} H {m} minutes")
else :
    if h!=23:
        print(f"Dans une minute il sera {h+1} H 00 minute ")
    else :
        print("Dans une minute il sera minuit ")

    