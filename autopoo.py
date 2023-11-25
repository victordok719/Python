class Auto:
    def __init__(self, placa,marca):
        self.placa = placa #atributo de instancia (propiedad)
        self.marca= marca

    def getplaca(self):
        return "Placa del auto es:", self.placa

    def setplaca(self,placa):    
        if len(placa)!= 6 or not isinstance(int(), int()):
            raise ValueError('La longitud debe ser igual a 6 y el valor ingresado')
        else :
            self.placa = placa

        

    def getmarca(self):
        print("Marca del auto: ", self.marca )
    
    def setmarca(self,marca):
        self.marca = marca

        


auto1=Auto("XYZ-26","BME")

print("Lod datos de auto 1 son: ")
#acceder al metodo para obtener la informacion de las propiedades
print(auto1.getplaca())

print(auto1.getmarca())







    