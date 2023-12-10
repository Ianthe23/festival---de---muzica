from termcolor import colored

class Festival:
    def __init__(self, name, month, ticket_cost, participants):
        """
        Functia constructor a clasei Festival
        :param name: numele festivalului
        :param month: luna in care are loc (1-12)
        :param ticket_cost: pretul biletului
        :param participants: o lista de participanti
        """

        self.__name = name
        self.__month = month
        self.__ticket_cost = ticket_cost
        self.__participants = participants

        """
        Getteri si setteri pt clasa Festival
        """

    def getName(self):
        return self.__name
    def getMonth(self):
        return self.__month
    def getTicket(self):
        return self.__ticket_cost
    def getParticipants(self):
        return self.__participants
        
    def setName(self, value):
        self.__name = value
    def setMonth(self, value):
        self.__month = value
    def setTicket(self, value):
        self.__ticket_cost = value
    def setParticipants(self, value):
        self.__participants = value

    def __eq__(self, other):
        return self.__name == other.__name and self.__month == other.__month and self.__ticket_cost == other.__ticket_cost and self.__participants == other.__participants
    def __str__(self):
        return colored("nume: ", "blue") + str(self.__name) + "; luna: " + str(self.__month) + "; pret bilet: " + str(self.__ticket_cost) + "; participanti: " + str(self.__participants) + colored("; ", "red")
    def __repr__(self):
        return str(self)
        
#test
def test_create_festival():
    festival = Festival("Born Pink", 4, 233, ["Rose", "Lisa", "Jennie", "Jisoo"])
    assert festival.getName() == "Born Pink"
    assert festival.getMonth() == 4
    assert festival.getTicket() == 233
    assert festival.getParticipants() == ["Rose", "Lisa", "Jennie", "Jisoo"]

test_create_festival()