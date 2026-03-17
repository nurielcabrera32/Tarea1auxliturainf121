# Ejercicio 5
# Nuriel Cabrera
# Version 1.0
class Aula:
    # ===== Constructor =====
    def __init__(self, nombre, piso, estudiantes):
        self.nombre = nombre
        self.piso = piso
        self.estudiantes = estudiantes
    # ===== Metodo sobrecargado =====
    def mostrar(self, opcion=None):
        # Mostrar todos los datos
        if opcion is None:
            print("Nombre del Aula:", self.nombre)
            print("Piso:", self.piso)
            print("Estudiantes y notas:")
            for est in self.estudiantes:
                print(est[0], "-", est[1])
        # Mostrar aprobado o reprobado
        elif opcion == "estado":
            print("Estado de los estudiantes:")
            for est in self.estudiantes:
                if est[1] >= 51:
                    print(est[0], "-", est[1], "- APROBADO")
                else:
                    print(est[0], "-", est[1], "- REPROBADO")
# ===== PRUEBA =====
estudiantes = [
    ["Ana", 80],
    ["Luis", 45],
    ["Carlos", 60],
    ["Maria", 30]
]
aula1 = Aula("Aula 101", 1, estudiantes)
print("\n--- Mostrar todos los datos ---")
aula1.mostrar()
print("\n--- Mostrar estado de estudiantes ---")
aula1.mostrar("estado")