### Notes
1. Proxy acts as a an interface for a main class. It encapsulates the main class and can provide additional functionality based on the main class.
2. We can use it to organize code and increase maintainability.
3. We can use to cache resource heavy operations that are done by the main class.


```python
from abc import ABC, abstractmethod
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
        self.cached_result = None
        
    def heavyload(self):
        if self.cached_result is None:
            self.cached_result = self.database.heavyload()
        return self.cached_result
        
        
def main():
    
    db = Database()
    
    database = DatabaseProxy(db)
    database.heavyload()
    database.heavyload() # This second call will return the cached result and won't execute the heavyload method again.
        

if __name__ == "__main__":
    main()

```