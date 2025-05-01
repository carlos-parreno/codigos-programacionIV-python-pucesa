# clase calificacion
class Calificacion:
    def __init__(self, materia, nota):
        self.materia = materia
        self.nota = nota
    
    def mostrar_datos(self):
        print(f"La materia {self.materia} tiene una nota de {self.nota}")