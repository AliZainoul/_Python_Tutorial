class Car:
  def __init__(self, make: str, model: str, year: int):
    if year <= 0:
      raise ValueError("Year cannot be negative or zero.")
    self.make = make
    self.model = model
    self.year = year
  
  def display(self):
    print(f"Your car is a {self.make} {self.model} from {self.year}.")

  def start(self):
    print(f"Your {self.make} {self.model} is starting.")

twingo = Car("Renault", "Twingo", 2015)
twingo.start()
twingo.display()