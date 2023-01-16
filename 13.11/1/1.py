<<<<<<< HEAD
tomb = []
file = open("13.11\\1\\regi.txt", "r")
for line in file:
    tomb.append(line)
file.close()

index = len(tomb) -1
tomb2 = []
for l in tomb:
    tomb2.append(tomb[index])
    index = index - 1

file = open("13.11\\1\\uj.txt", "w")
for x in tomb2:
    file.writelines(x)
=======
tomb = []
file = open("13.11\\1\\regi.txt", "r")
for line in file:
    tomb.append(line)
file.close()

index = len(tomb) -1
tomb2 = []
for l in tomb:
    tomb2.append(tomb[index])
    index = index - 1

file = open("13.11\\1\\uj.txt", "w")
for x in tomb2:
    file.writelines(x)
>>>>>>> f816dcd7997840446aed11088e1d8c9a3f1db076
file.close()