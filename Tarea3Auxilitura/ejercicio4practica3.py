# Ejercicio 4
# Nuriel Cabrera
# Version 1.0
# Clase Videojuego
class Videojuego:
    # ===== Constructor sobrecargado =====
    def __init__(self, nombre=None, plataforma=None, jugadores=0):
        self.nombre = nombre
        self.plataforma = plataforma
        self.jugadores = jugadores
    # ===== Metodo para agregar jugadores =====
    def agregarJugadores(self, cantidad=1):
        self.jugadores += cantidad
        print("Jugadores agregados:", cantidad)
    # ===== Mostrar datos =====
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Plataforma:", self.plataforma)
        print("Cantidad de jugadores:", self.jugadores)
# ===== PRUEBA DEL PROGRAMA =====
# Instancia 1
juego1 = Videojuego("FIFA 24", "PlayStation", 2)
# Instancia 2
juego2 = Videojuego("Minecraft", "PC")
# Agregar un jugador
juego1.agregarJugadores()
# Agregar varios jugadores
juego2.agregarJugadores(3)
print("\nDatos del Juego 1")
juego1.mostrar()
print("\nDatos del Juego 2")
juego2.mostrar()