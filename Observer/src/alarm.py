from typing import Type
from .interfaces import Observer

class Alarme:
    def __init__(self):
        self.beep = False
        self.pessoal_dormindo = []
    
    def addUser(self, user: Type[Observer]):
        self.pessoal_dormindo.append(user)
    
    def estadoAlarm(self):
        return self.beep
    
    def tocarAlarm(self):
        self.beep = True
        for u in self.pessoal_dormindo:
            u.update()
        
        self.pessoal_dormindo = []