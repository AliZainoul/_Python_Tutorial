class Car:
    def __init__(self, make_value, model_value, year_value):
        self.make = make_value 
        self.model = model_value 
        self.year = year_value

    def get_make(self): 
        return self.make

    def get_model(self): 
        return self.model

    def get_year(self): 
        return self.year

    def set_make(self, make_value): 
        self.make = make_value

    def set_model(self, model_value): 
        self.model = model_value
        
    def set_year(self, year_value): 
        self.year = year_value

    def set_all(self, make_value, model_value, year_value):
        self.set_make(make_value)
        self.set_model(model_value)
        self.set_year(year_value)
        
    def __repr__(self):
        return f"{type(self).__name__}\
        (make='{self.make}', model={self.model}, year={self.year})"
