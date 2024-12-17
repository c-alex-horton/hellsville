from app.db.db import db
from app.controller.town_manager import TownManager

db.connect()

manager = TownManager()
manager.get_population()