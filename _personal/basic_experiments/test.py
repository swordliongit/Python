from abc import ABC, abstractmethod
from functools import lru_cache
from time import sleep


class Interface(ABC):
    
    @abstractmethod
    def heavyload(self):
        pass
    
    
class Database(Interface):

    def heavyload(self):
        sleep(5)
        print("Printed from the Database")
        

class DatabaseProxy(Interface):
    
    def __init__(self, Database):
        self.database = Database
        
    @lru_cache
    def heavyload(self):
        self.database.heavyload()
        
        
def main():
    
    db = Database()
    
    database = DatabaseProxy(db)
    database.heavyload()
        


if __name__ == "__main__":
    main()