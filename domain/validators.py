from domain.entities import Festival
from termcolor import colored

class FestivalValidator:
    def valideaza_festivalul(self, festival):
        erori = []
        if festival.getName() == "":
            erori.append(colored("Numele festivalului nu poate fi vid!", "red"))
        if festival.getMonth() < 1 or festival.getMonth() > 12:
            erori.append(colored("Luna trebuie sa fie intre 1 si 12!", "red"))
        if festival.getTicket() < 0:
            erori.append(colored("Pretul biletului nu poate fi negativ!", "red"))
        if festival.getParticipants() == []:
            erori.append(colored("Lista de participanti nu poate fi vida!", "red"))

        if len(erori) > 0:
            raise ValueError(erori[0])
        
#teste
def test_FestivalValidator():
    validator = FestivalValidator()

    festival = Festival("Born Pink", 4, 233, ["Rose", "Lisa", "Jennie", "Jisoo"])
    validator.valideaza_festivalul(festival)

    festival = Festival("", 4, 233, ["Rose", "Lisa", "Jennie", "Jisoo"])
    try:
        validator.valideaza_festivalul(festival)
        assert False
    except ValueError:
        assert True

    festival = Festival("Born Pink", 0, 233, ["Rose", "Lisa", "Jennie", "Jisoo"])
    try:
        validator.valideaza_festivalul(festival)
        assert False
    except ValueError:
        assert True
    
    festival = Festival("Born Pink", 4, -22, ["Rose", "Lisa", "Jennie", "Jisoo"])
    try:
        validator.valideaza_festivalul(festival)
        assert False
    except ValueError:
        assert True

    festival = Festival("Born Pink", 4, 233, [])
    try:
        validator.valideaza_festivalul(festival)
        assert False
    except ValueError:
        assert True

test_FestivalValidator()