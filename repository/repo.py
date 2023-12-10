from domain.entities import Festival
from domain.validators import FestivalValidator
import os
from termcolor import colored

class OperatiiFestivalFile:
    def __init__(self, filename):
        """
        Metoda constructor a clasei OperatiiFestivalFile
        :param filename: fisierul cu festivalurile
        """
        self.__festivals = []
        file = os.path.abspath(filename)
        self.__filename = file
        self.__load_from_file()

    def __load_from_file(self):
        """
        Citim datele din fisier
        """
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line == "\n":
                    break
                name, month, ticket_cost, participants = [elem.strip() for elem in line.split(", ")]
                participant = [elem.strip() for elem in participants.split(' ')]
                festival = Festival(name, month, ticket_cost, participant)
                self.__festivals.append(festival)

    def __save_to_file(self):
        """
        Salvam datele in fisier
        """
        with open(self.__filename, "w") as f:
            toate_festivalurile = self.returneaza_festivaluri()
            for festival in toate_festivalurile:
                festival_de_salvat = str(festival.getName()) + ", " + str(festival.getMonth()) + ", " + str(festival.getTicket()) + ", "

                str_participants = ""
                for participant in festival.getParticipants():
                    str_participants += str(participant) + ' '
                    
                festival_de_salvat += str_participants + "\n"
                f.write(festival_de_salvat)

    def adauga_festival(self, festival_nou):
        """
        Adaugam un festival nou
        :param festival_nou: festivalul de adaugat
        """
        for festival in self.__festivals:
            if festival.getName() == festival_nou.getName():
                raise ValueError(colored("Numele festivalului exista deja!", "red"))
        self.__festivals.append(festival_nou)
        self.__save_to_file()

    def returneaza_festivaluri(self):
        return self.__festivals

    def __eq__(self, other):
        return self.__festivals == other.__festivals
    
#teste

def test_adauga_festival():
    repo = OperatiiFestivalFile("test_repo.txt")
    assert repo.returneaza_festivaluri() == []
    
    festival = Festival("Born Pink", 4, 233, ["Rose", "Lisa", "Jennie", "Jisoo"])
    repo.adauga_festival(festival)
    assert len(repo.returneaza_festivaluri()) == 1

test_adauga_festival()
