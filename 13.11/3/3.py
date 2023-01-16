tomb = []
file = open("13.11\\3\\valami.txt", "r", encoding="utf-8")
for line in file:
    tomb.append(line)
file.close()

tomb2 = []
file = open("13.11\\3\\valami2.txt", "w", encoding="utf-8")
for line in file:
    tomb.append(line)
file.close()

