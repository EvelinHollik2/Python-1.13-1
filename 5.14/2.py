napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
nap= int(input("Hány napra mész el?"))
melyik = int(input("melyik nap indulsz?"))
szam=0
szam= (nap+melyik)%7
napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
nap= int(input("Hány napra mész el?"))
melyik = int(input("melyik nap indulsz?"))
szam=0
szam= (nap+melyik)%7
print(f"{napok[szam]}i napon ersz haza")