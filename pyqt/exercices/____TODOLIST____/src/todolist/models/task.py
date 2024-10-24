class Task:
    """
    A class to represent a task in a to-do list.

    Attributes:
    -----------
    _name : str
        The name of the task.
    _is_done : bool
        A boolean indicating whether the task is done or not.

    Methods:
    --------
    name (property):
        Gets the task's name.
    name (setter):
        Sets the task's name, ensuring it is a string and different from the current name.
    is_done (property):
        Gets the task's status (done or not).
    is_done (setter):
        Sets the task's status, ensuring it is a boolean and different from the current status.
    __str__():
        Returns a string representation of the task.
    """
    
    def __init__(self, name: str = "", is_done: bool = False):
        """
        Initializes a Task object with a name and status (done or not).

        Parameters:
        -----------
        name : str, optional
            The name of the task (default is an empty string).
        is_done : bool, optional
            The status of the task (default is False, meaning the task is not done).
        """
        self._name: str = name
        self._is_done: bool = is_done

    @property
    def name(self) -> str:
        """
        Gets the name of the task.

        Returns:
        --------
        str:
            The name of the task.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Sets the name of the task, ensuring it is a string and different from the current name.

        Parameters:
        -----------
        new_name : str
            The new name to set for the task.

        Raises:
        -------
        TypeError:
            If the new name is not a string.
        """
        if isinstance(new_name, str):
            if new_name != self.name:
                self._name = new_name
        else:
            raise TypeError("The new name must be a string.\n")

    @property
    def is_done(self) -> bool:
        """
        Gets the task's status (whether it is done or not).

        Returns:
        --------
        bool:
            True if the task is done, False otherwise.
        """
        return self._is_done

    @is_done.setter
    def is_done(self, new_status: bool) -> None:
        """
        Sets the task's status, ensuring it is a boolean and different from the current status.

        Parameters:
        -----------
        new_status : bool
            The new status to set for the task.

        Raises:
        -------
        TypeError:
            If the new status is not a boolean.
        """
        if isinstance(new_status, bool):
            if new_status != self.is_done:
                self._is_done = new_status
        else:
            raise TypeError("The new status (is_done) must be a boolean.\n")

    def __str__(self) -> str:
        """
        Returns a string representation of the task.

        Returns:
        --------
        str:
            A string representation of the task, including its name and status.
        """
        return f"Task name: {self.name} and its status is {self.is_done}.\n"