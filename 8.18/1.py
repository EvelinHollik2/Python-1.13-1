#"Python"[1]
#"A sztringek karaktersorozatok."[5]
#len("csodálatos")
#"Rejtély"[:4]
#szerepel_e = "k"in"Körte"
#print(szerepel_e)
#szerepel_e = "barack"in"sárgabarack"
#print(szerepel_e)
#szerepel_e = "körte"not in"Ananász"
#print(szerepel_e)
#"barack" > "sárgabarack"
#"ananász" < "Barack"

#2.py
#elotag = "Törp"
#utotagok_listaja = ["erős", "költő", "morgó", "öltő", "apa", "icur", "szakáll"]
#                                    
#for utotag in utotagok_listaja:
#    print(elotag + utotag)

#3.py
#def karakter_szamlalas(gyumolcs, darab):
#    gyumolcs = "banán"
#    darab=0
#    for karakter in gyumolcs:
#        if karakter == "a":
#            darab += 1
#    print(darab)

#6.py
#elrendezes = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"#

#print(elrendezes.format("i", "i**2", "i**3", "i**4", "i**5", "i**6", "i**7", "i**8", "i**9", "i**10", "i**11", "i**12"))
#for i in range(1, 11):
#    print(elrendezes.format(i, i**2, i**3, i**4, i**5, i**6, i**7, i**8, i**9, i**10, i**11, i**12))

#7.py
#def sztring_forditas(val):
#    return val[::-1]

#print(sztring_forditas("boldog"))
#print(sztring_forditas("Python"))
#print(sztring_forditas(""))
#print(sztring_forditas("a"))

#9.py
#def betu_eltuntetes():
    
#print(betu_eltuntetes("a", "alma"))
#print(betu_eltuntetes("a", "banán"))
#print(betu_eltuntetes("z", "banán"))
#print(betu_eltuntetes("e", "Kerepes"))
#print(betu_eltuntetes("b", ""))
#print(betu_eltuntetes("b", "c"))


#11.py
#def szamlalas():
#
#print(szamlalas("gö", "görögös"))
#print(szamlalas("pa", "papaja"))
#print(szamlalas("apa", "papaja"))
#print(szamlalas("papa", "papaja"))
#print(szamlalas("apap", "papaja"))
#print(szamlalas("aaa", "aaaaaa"))


#12.py
