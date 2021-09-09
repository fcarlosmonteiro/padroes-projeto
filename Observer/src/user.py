from .interfaces import Observer

class Usuario(Observer):
    def __init__(self):
        self.acordado = False
    
    def check_sono(self):
        return self.acordado
    
    def update(self):
        print("Acordando")
        self.acordado = True 