class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color
    
class TwoDimensional(Shape):
    def __init__(self, name, color, sides):
        super().__init__(name, color) 
        self.sides = sides

    def get_sides(self):
        return self.sides
    
class ThreeDimensional(Shape):
    def __init__(self, name, color, faces):
        super().__init__(name, color) 
        self.faces = faces
    def get_faces(self):
        return self.faces
    
# Hierarchical Inheritance
class Sphere(ThreeDimensional):
    def __init__(self, name, color, faces, radius):
        super().__init__(name, color, faces) 
        self.radius = radius
    def get_radius(self):
        return self.radius
    
ShapeA = Sphere('Sphere 1', 'Blue', 'Has no faces', '20 M')
print('Name\t: ',ShapeA.get_name())
print('Color\t: ',ShapeA.get_color())
print('Faces\t: ',ShapeA.get_faces())
print('Radius\t: ',ShapeA.get_radius())