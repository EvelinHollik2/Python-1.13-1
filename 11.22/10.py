<<<<<<< HEAD
class teszt:
    def cserel(s, regi, uj):
        teszt(cserel("Mississippi", "i", "I") == "MIssIssIppI")
        
        s = "Kerek a gömb, gömbszer ̋u!"
        teszt(cserel(s, "öm", "om") ==
        "Kerek a gomb, gombszer ̋u!")

        teszt(cserel(s, "o", "ö") ==
        "Kerek a gömb, gömbszer ̋u!")


=======
class teszt:
    def cserel(s, regi, uj):
        teszt(cserel("Mississippi", "i", "I") == "MIssIssIppI")
        
        s = "Kerek a gömb, gömbszer ̋u!"
        teszt(cserel(s, "öm", "om") ==
        "Kerek a gomb, gombszer ̋u!")

        teszt(cserel(s, "o", "ö") ==
        "Kerek a gömb, gömbszer ̋u!")


>>>>>>> 9e7bb9d2a3ed0d0b7619a60a492d1260ba593f83
print(teszt.cserel())