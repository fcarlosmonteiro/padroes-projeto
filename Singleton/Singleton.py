class Singleton(object):
    def __new__(cls): #instancia objeto
        if not hasattr(cls, 'instance'): #verifica se o objeto ja existe
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print("Objeto criado", s)

s1 = Singleton()
print("Objeto criado", s1)