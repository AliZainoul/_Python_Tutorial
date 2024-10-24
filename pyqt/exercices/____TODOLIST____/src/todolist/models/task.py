class Task:
    def __init__(self, name: str = "", is_done: bool = False):
        self._name      : str           = name
        self._is_done   : bool          = is_done 

    # Getter
    @property
    def name(self) -> str:
        return self._name
    
    # Equivalent to:
    # def get_name(self) -> str:
    #     return self._name

    # Setter
    @name.setter
    def name(self, new_name: str) -> None:
        if isinstance(new_name, str):
            if new_name != self.name:
                self._name = new_name
        else:
            raise TypeError("The new name must be a string. \n")
        
    # Equivalent to:
    # def set_name(self, new_name: str) -> None:
    # if isinstance(new_name, str):
    #     if new_name != self.name:
    #         self._name = new_name
    # else:
    #     raise TypeError("The new name must be a string. \n")
    
    # Getter
    @property
    def is_done(self) -> bool:
        return self._is_done
    
    # Setter
    @is_done.setter
    def is_done(self, new_status: bool) -> None:
        if isinstance(new_status, bool):
            if new_status != self.is_done:
                self._is_done = new_status
        else:
            raise TypeError("The new status (is_done) must be a boolean. \n")
        
    def __str__(self) -> str:
        return f"Task name: {self.name} and it's status is {self.is_done} \n"