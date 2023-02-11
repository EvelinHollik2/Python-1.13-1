<<<<<<< HEAD:ág gyak/emberek.py
import random
class Ember():
    def __init__(self, nev, foglalkozas, nem, szam):
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nem = nem
        self.szam = szam

    def fvn(nem):
        if nem =="f":
            return "Férfi"
        elif nem =="n":
            return "Nő"

t=[]
for x in range(3):
    a=input("Add meg a nevet! ")
    b=input("Add meg a foglalkozását! ")
    c=input("Add meg a nemét! ")
    d=random.randint(1,50)
    t.append(Ember(a,b,c,d))

for x in range(3):
    print(t[x].nev,"")
    print(a, b, c, "szerencseszáma a", d)
=======
import random
class Ember():
    def __init__(self, nev, foglalkozas, nem, szam):
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nem = nem
        self.szam = szam

    def fvn(nem):
        if nem =="f":
            return "Férfi"
        elif nem =="n":
            return "Nő"

t=[]
for x in range(3):
    a=input("Add meg a nevet! ")
    b=input("Add meg a foglalkozását! ")
    c=input("Add meg a nemét! ")
    d=random.randint(1,50)
    t.append(Ember(a,b,c,d))

pointer = open("emberek_lista.txt", "w")
for x in range(3):
    print(t[x].nev,"")
    print(a, b, c, "szerencseszáma a", d)
    pointer.write(a, b, c, "szerencseszáma a", d \n)
pointer.close()
>>>>>>> 789bb7d1da7f0d9fc9fa84596aec9b2e37d368ef:ág gyak/emberek 3/emberek.py
