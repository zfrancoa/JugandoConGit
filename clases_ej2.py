
class Vehicle:
    def __init__(self, marca, color, modelo):
        self.marca = marca
        self.color = color
        self.modelo = modelo

    def max_velocidad(self, val_max_marcador):
        return val_max_marcador*2

for name in Vehicle.__dict__:
    print(name)