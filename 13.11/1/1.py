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
file.close()