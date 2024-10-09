import math

class Circle :
    def __init__ (self, radius:float = 0.0):
        self._radius = radius
        
    
    def get_radius (self):
        print(self._radius)
        return self._radius
    
    def set_radius (self):
        try :
            new_radius = float(input("Entrez rayon : "))
            if new_radius < 0.0 :
                print("entrez une valeur correcte ! ")
                self.set_radius()
            else :
                self._radius = new_radius
        except :
            print("Entrez une valeur correcte !")
            self.set_radius()
    
    def area(self) :
        r = self.get_radius()
        area = r * r * math.pi
        print ("Aire : ", area)
        return area    

my_circle = Circle(5.5)
my_circle.set_radius()
my_circle.get_radius()
my_circle.area()  