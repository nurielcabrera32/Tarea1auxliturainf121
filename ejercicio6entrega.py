class Pantalla:
    def __init__(self, tipo, ancho, alto):
        self.tipo = tipo
        self.ancho = ancho
        self.alto = alto

    def __str__(self):
        return f"Pantalla: {self.tipo}, {self.ancho}x{self.alto}"


class Aplicacion:
    def __init__(self, nombre, tamanio):
        self.nombre = nombre
        self.tamanio = tamanio

    def __str__(self):
        return f"{self.nombre} ({self.tamanio}MB)"


class Laptop:
    def __init__(self, modelo, pantalla):
        self.modelo = modelo
        self.pantalla = pantalla
        self.apps = []

    def agregar_app(self, app):
        self.apps.append(app)

    def mostrar_apps(self):
        print(f"Aplicaciones de {self.modelo}:")
        for app in self.apps:
            print(app)

    def eliminar_apps_por_ancho(self, ancho):
        if self.pantalla.ancho == ancho:
            self.apps.clear()

    def cantidad_apps(self):
        return len(self.apps)

    def __str__(self):
        return f"Laptop {self.modelo} - {self.pantalla} - Apps: {len(self.apps)}"