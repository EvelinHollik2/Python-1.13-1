tomb = []
file = open("13.11\\2\\masik.txt", "r", encoding="utf-8")
for line in file:
    tomb.append(line)
file.close()

for line in tomb:
    if "info" in line:
        print(line)
