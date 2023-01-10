class teszt:
    def cserel(s, regi, uj):
        teszt(cserel("Mississippi", "i", "I") == "MIssIssIppI")
        
        s = "Kerek a gömb, gömbszer ̋u!"
        teszt(cserel(s, "öm", "om") ==
        "Kerek a gomb, gombszer ̋u!")

        teszt(cserel(s, "o", "ö") ==
        "Kerek a gömb, gömbszer ̋u!")


print(teszt.cserel())