<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> f816dcd7997840446aed11088e1d8c9a3f1db076

#def szo_tisztitas(szo):
#    spec = "\'\"+!%/=()~ˇ^˘°˛`˙´,.-?:_;>*>#&@\\{}łŁ$ß÷đĐ[]€"
#    spec = [*spec]
#    for s in spec:
#        szo = "".join(szo.split(s))
#    return szo
#print(szo_tisztitas("hogyan?"))
#print(szo_tisztitas("'most!'"))
#print(szo_tisztitas("?+='s-z-a-v!a,k@$()'"))

#def van_duplavonal(szo):
#    spec = "-"
#    spec = [*spec]
#    if "--" in spec:
#        return True
#    elif "-" in spec:
#        return False
#    return szo
#print(van_duplavonal("kicsi--nagy"))
#print(van_duplavonal(""))
#print(van_duplavonal("magas--"))
#print(van_duplavonal("piros--fekete"))
#print(van_duplavonal("-igen-nem-"))

def szavakra_bontas(szo):
    szo.seed()
    return szo[0]+''.join([ szavakra_bontas()+kar for kar in szo[1:] ])
print(szavakra_bontas(" Most van itt az id ̋o? Igen, most."))
print(szavakra_bontas(" ̋O megpróbált udariasan viselkedni!"))
<<<<<<< HEAD

#def szo_tisztitas(szo):
#    spec = "\'\"+!%/=()~ˇ^˘°˛`˙´,.-?:_;>*>#&@\\{}łŁ$ß÷đĐ[]€"
#    spec = [*spec]
#    for s in spec:
#        szo = "".join(szo.split(s))
#    return szo
#print(szo_tisztitas("hogyan?"))
#print(szo_tisztitas("'most!'"))
#print(szo_tisztitas("?+='s-z-a-v!a,k@$()'"))

#def van_duplavonal(szo):
#    spec = "-"
#    spec = [*spec]
#    if "--" in spec:
#        return True
#    elif "-" in spec:
#        return False
#    return szo
#print(van_duplavonal("kicsi--nagy"))
#print(van_duplavonal(""))
#print(van_duplavonal("magas--"))
#print(van_duplavonal("piros--fekete"))
#print(van_duplavonal("-igen-nem-"))

def szavakra_bontas(szo):
    szo.seed()
    return szo[0]+''.join([ szavakra_bontas()+kar for kar in szo[1:] ])
print(szavakra_bontas(" Most van itt az id ̋o? Igen, most."))
print(szavakra_bontas(" ̋O megpróbált udariasan viselkedni!"))
=======
=======

#def szo_tisztitas(szo):
#    spec = "\'\"+!%/=()~ˇ^˘°˛`˙´,.-?:_;>*>#&@\\{}łŁ$ß÷đĐ[]€"
#    spec = [*spec]
#    for s in spec:
#        szo = "".join(szo.split(s))
#    return szo
#print(szo_tisztitas("hogyan?"))
#print(szo_tisztitas("'most!'"))
#print(szo_tisztitas("?+='s-z-a-v!a,k@$()'"))

#def van_duplavonal(szo):
#    spec = "-"
#    spec = [*spec]
#    if "--" in spec:
#        return True
#    elif "-" in spec:
#        return False
#    return szo
#print(van_duplavonal("kicsi--nagy"))
#print(van_duplavonal(""))
#print(van_duplavonal("magas--"))
#print(van_duplavonal("piros--fekete"))
#print(van_duplavonal("-igen-nem-"))

def szavakra_bontas(szo):
    szo.seed()
    return szo[0]+''.join([ szavakra_bontas()+kar for kar in szo[1:] ])
print(szavakra_bontas(" Most van itt az id ̋o? Igen, most."))
print(szavakra_bontas(" ̋O megpróbált udariasan viselkedni!"))
>>>>>>> 9e7bb9d2a3ed0d0b7619a60a492d1260ba593f83
>>>>>>> f816dcd7997840446aed11088e1d8c9a3f1db076
