class Singleton:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
        
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1)
print(singleton2)
