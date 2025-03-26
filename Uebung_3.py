import math

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def dist_to(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
    def __str__(self):
        return f"({self.x},{self.y})"

class Figur:
    def __init__(self):
        self.name = "Figur"

    def Umfang(self):
        return 0
    
    def __str__(self):
        return self.name
    
class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__()
        self.name = "Kreis"
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def Umfang(self):
        return self.radius * 2 * math.pi
    
    def __str__(self):
        return f"{self.name} M={self.mittelpunkt} r={self.radius}"

class Rechteck(Figur):
    def __init__(self, a, b):
        super().__init__()
        self.name = "Rechteck"
        self.a = a
        self.b = b

    def Umfang(self):
        return 2 * (abs(self.b.x - self.a.x) + abs(self.b.y - self.a.y))
    
    def __str__(self):
        return f"{self.name} {self.a} - {self.b}"
    
class Dreieck(Figur):
    def __init__(self, c, d, e):
        super().__init__()
        self.name = "Dreieck"
        self.c = c
        self.d = d
        self.e = e
    
    def Umfang(self):
        return self.c.dist_to(self.d) + self.d.dist_to(self.e) + self.e.dist_to(self.c)
    
    def __str__(self):
         return f"{self.name} {self.c} - {self.d} - {self.e}"
    
class Polygon(Figur):
    def __init__(self, punkte):
        super().__init__()
        self.name = "Polygon"
        self.punkte = punkte

    def Umfang(self):
        umfang = 0
        for i in range(len(self.punkte)):
            umfang += self.punkte[i].dist_to(self.punkte[(i + 1) % len(self.punkte)])
        return umfang
    
    def __str__(self):
        punkte_str = ' - '.join(str(p) for p in self.punkte)
        return f"{self.name} {punkte_str}"
    

m = Point(2.3,4.2)
kreis = Kreis(m, 3.4)
print(kreis)
print(kreis.Umfang())

a = Point(0, 0)
b = Point(10, 15)
rechteck = Rechteck(a, b)
print(rechteck)
print(rechteck.Umfang())

c = Point(0, 0)
d = Point(3, 0)
e = Point(3, 4)
dreieck = Dreieck(c, d, e)
print(dreieck)
print(dreieck.Umfang())

punkte = [Point(0, 0), Point(4, 0), Point(4, 3), Point(0, 3)]
polygon = Polygon(punkte)
print(polygon)
print(polygon.Umfang())

figuren = [kreis, rechteck, dreieck, polygon]   # Alles zusammen
for figur in figuren:
    print(f"{figur} -> Umfang: {figur.Umfang():.2f}")
