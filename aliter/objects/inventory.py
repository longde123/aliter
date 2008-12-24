from sqlalchemy import *
from sqlalchemy.orm import relation, backref

from aliter.db import Base

from character import Character


class InventoryItem(Base):
    __tablename__ = "inventory"
    
    id = Column(Integer, primary_key = True)
    characterID = Column(Integer, ForeignKey("characters.id"))
    itemID = Column(Integer, ForeignKey("items.id"))
    amount = Column(Integer, default = 1)
    equipLocation = Column(Integer)
    identified = Column(Boolean, default = True)
    refine = Column(Integer)
    broken = Column(Integer)
    forger = Column(Integer, ForeignKey("characters.id"))
    element = Column(Integer)
    very = Column(Integer)
    card1 = Column(Integer)
    card2 = Column(Integer)
    card3 = Column(Integer)
    card4 = Column(Integer)
    
    character = relation(Character, backref = backref("inventory"))
