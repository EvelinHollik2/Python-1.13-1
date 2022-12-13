def konyvek(a):        
    b = False
    if oldal > 150:
        b = True
    return b

cím = input("Add meg a könyv címét! ")
while (cím != " "):
    oldal = int(input("Add meg az oldalainak számát! "))
    if oldal > 150:
        print("A", cím, "hosszú tejedelmű könyv")
    else:
        print("A", cím, "rövid tejedelmű könyv")
    cím=input ("Add meg a könyv címét! ")
