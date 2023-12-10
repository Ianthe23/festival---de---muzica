from domain.entities import Festival
from domain.validators import FestivalValidator
from repository.repo import OperatiiFestivalFile
from service.service import FestivalService
from ui.console import Console

festival = FestivalService(OperatiiFestivalFile("festival.txt"), FestivalValidator())

ui = Console(festival)

ui.show_ui()