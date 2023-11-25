class Alumno:
    
    def declarar(self,nombre,dato):
        self.nombre=nombre   #fundamental la palabra self para los atributos
        self.puntuacion=dato

    def visualizar(self):
        print("Nombre:",self.nombre)
        print("Puntuacion:",self.puntuacion)

    def estadistica(self):
        if self.puntuacion<=4:
            print("insuficiente")
        elif self.puntuacion>=5:
            print("Notable")
        elif self.puntuacion>=8:
            print("sobresaliente")
        else:
            print("Libre")



#bloque principal

alumno1=Alumno()
alumno1.declarar("diego",2)
alumno1.visualizar()
alumno1.estadistica()

alumno2=Alumno()
alumno2.declarar("anna",10)
alumno2.visualizar()
alumno2.estadistica()