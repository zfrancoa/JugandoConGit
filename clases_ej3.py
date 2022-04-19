class Vehicle:
    def __init__(self, marca, color, modelo):
        self.marca = marca
        self.color = color
        self.modelo = modelo

    def max_velocidad(self, val_max_marcador):
        return val_max_marcador*2


instance = Vehicle('Ferrari', 'red', 2021)#instancia

#muestre el espacio de nombres de dicha instancia:
print(instance.__dict__)
