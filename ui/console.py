from termcolor import colored

def printMeniu():
    """
    Afisam meniul
    """
    print("Va rugam alegeti o optiune de mai jos:")
    print("   1) adaugati un festival;")
    print("   2) afisati festivalurile care au loc intr-un anumit anotimp;")
    print("   3) afisati festivalurile care au acelasi participant;")
    print("   0) iesiti din aplicatie.")

class Console:
    def __init__(self, srv):
        """
        Initializam consola pentrun a lucra cu controllerul GRASP
        :param srv: service-ul festivalurilor
        """

        self.__srv = srv

    def __add_festival(self):
        """
        Adaugam un festival nou
        """
        try:
            name = input("Introduceti numele festivalului: ")
            month = int(input("Introduceti luna in care are loc: "))
            ticket_cost = int(input("Introduceti costul unui bilet: "))
            participanti = [participant for participant in input("Introduceti participantii: ").split()]

            festival = self.__srv.add_festival(name, month, ticket_cost, participanti)
        except ValueError as ve:
            print(ve)

    def __show_festivals_season(self):
        """
        Afisam festivalurile care au loc in acelasi anotimp
        """
        try:
            season = input("Introduceti anotimpul: ")
            raport = self.__srv.show_festivals_season(season)

            underlined_string ="    " + "\033[4m" + "Raportul privind festivalurile care au loc in acelasi anotimp dat" + "\033[0m"
            print("\n")
            print(colored(underlined_string, "cyan"))
            print("\n")
            for elem in raport:
                print(colored("nume: ", "blue"), end = " ")
                print(elem[0], end = "  ")
                print(colored("luna: ", "green"), end = " ")
                print(elem[1], end = "  ")
                print(colored("costul biletului: ", "yellow"), end = " ")
                print(elem[2], end = "  ")
                print(colored("participanti: ", "magenta"), end = " ")
                for index in range(len(elem[3])):
                    if index != len(elem[3]) - 1:
                        print(elem[3][index], end = " ")
                    else:
                        print(elem[3][index])
        except ValueError as ve:
            print(ve)

    def __show_festivals_participants(self):
        """
        Afisam festivalurile la care participa acelasi participant
        """
        participant = input("Introduceti participantul: ")
        raport = self.__srv.show_festivals_participant(participant)

        underlined_string ="    " + "\033[4m" + str(colored("Raportul privind festivalurile la care participa acelasi participant", "cyan")) + "\033[0m"
        print("\n")
        print(underlined_string)
        print("\n")

        for elem in raport:
            print(colored("nume: ", "blue"), end = " ")
            print(elem[0], end = "  ")
            print(colored("luna: ", "green"), end = " ")
            print(elem[1], end = "  ")
            print(colored("costul biletului: ", "yellow"), end = " ")
            print(elem[2], end = "  ")
            print(colored("participanti: ", "magenta"), end = " ")
            for index in range(len(elem[3])):
                if index != len(elem[3]) - 1:
                    print(elem[3][index], end = " ")
                else:
                    print(elem[3][index])
            
    
    def __show_all(self):
        """
        Returnam toate festivalurile
        """
        return self.__srv.get_all()

    def show_ui(self):
        print("\n")
        print("Bine ati venit la festivalurile din 2024!\n")

        exit = False
        while not (exit):
            print("\n")
            print("Lista de festivaluri: ", self.__show_all())
            print("\n")

            printMeniu()
            optiune = input("Introduceti optiunea: ").strip()
            if optiune == '0':
                print("\nLa revedere!")
                exit = True
            else:
                if optiune == '1':
                    self.__add_festival()
                elif optiune == '2':
                    self.__show_festivals_season()
                elif optiune == '3':
                    self.__show_festivals_participants()
                else:
                    print(colored("Comanda invalida!", "red"), "\n")




                        