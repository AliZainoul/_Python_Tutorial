class IDD:
    # Constructor (only 1):
    def __init__(self, id_ : int):
        self.id = id_
    
    # Getter
    def get_id (self) -> int:
        return self.id
    
    # Setter
    def set_id (self, id_ : int) -> None:
        self.id = id_

    # Helpers
    def returnInfos(self) -> list:
        return [f"ID = {self.get_id()}", f"{self}", f"{type(self)}"]
    
    # MAGIC METHOD REPR for DEVS (dev-friendly):
    def __repr__(self) -> str:
       return f"ID = {self.id}"
    
    # MAGIC METHOD STR for USERS (user-friendly):
    def __str__(self) -> str:
       return f"The ID is: {self.id}, have a good day!"
# END OF CLASS

object_idd = IDD(1)
print(object_idd.returnInfos())
print(repr(object_idd))
print(str(object_idd))

object_idd.set_id(2)
print(object_idd.returnInfos())
print(repr(object_idd))
print(str(object_idd))
