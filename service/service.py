from domain.entities import Festival
from domain.validators import FestivalValidator
from repository.repo import OperatiiFestivalFile
from termcolor import colored
import calendar

class FestivalService:
    def __init__(self, repo, validator):
        """
        Metode constructor pt controllerul GRASP
        :param repo: repository-ul
        :param validator: validatorul
        """
        self.__repo = repo
        self.__validator = validator

    def add_festival(self, nume, month, ticket_cost, participants):
        """
        Incercam sa introducem festivalul in memorie
        :param nume: numele festivalului
        :param month: luna festivalului
        :param ticket_cost: pretul biletului
        :param participants: lista de participanti
        """
        festival = Festival(nume, month, ticket_cost, participants)
        self.__validator.valideaza_festivalul(festival)
        self.__repo.adauga_festival(festival)
        return festival
    
    def create_raport(self):
        """
        Creeam raport privind festivalurile
        """
        lista = self.__repo.returneaza_festivaluri()
        raport = []
        for festival in lista:
            raport.append([festival.getName(), int(festival.getMonth()), int(festival.getTicket()), festival.getParticipants()])
        return raport
    
    def show_festivals_season(self, season):
        """
        Afisam raportul festivalurilor care au loc intr-un anumit anotimp
        :param season: anotimpul dorit
        """

        lista = self.create_raport()
        lista_sortata = sorted(lista, key = lambda x: (x[1], x[0]))
        raport = []

        if season == "winter":
            luni = [1, 2, 12]
        elif season == "spring":
            luni = [3, 4, 5]
        elif season == "summer":
            luni = [6, 7, 8]
        elif season == "autumn" or season == "fall":
            luni = [9, 10, 11]
        else:
            raise ValueError(colored("Anotimpul nu a fost introdus corect!", "red"))
        for festival in lista_sortata:
            ok = 1
            for luna in luni:
                if festival[1] == luna:
                    ok = 0
                    luna_nume = calendar.month_name[festival[1]]
                    break
            if ok == 0:
                raport.append([festival[0], luna_nume, festival[2], festival[3]])
        
        return raport
    
    def show_festivals_participant(self, participant_dorit):
        """
        Afisam raportul festivalurilor ce contin acelasi participant
        :param participant_dorit: participantul dorit
        """

        lista = self.create_raport()
        lista_sortata = sorted(lista, key = lambda x: x[1])
        raport = []

        for festival in lista_sortata:
            for participant in festival[3]:
                if participant == participant_dorit:
                    raport.append(festival)

        return raport

    def get_all(self):
        """
        Returnam toate festivalurile
        """
        return self.__repo.returneaza_festivaluri()

