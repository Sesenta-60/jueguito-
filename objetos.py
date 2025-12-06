class personaje:
    def __init__(self,nombre,,clase,vidam,manam,estadisticas,puntos=0):
        self.nombre=nombre
        self.vida=vidam
        self.mana=manam
        self.estadisticas=estadisticas
        self.daño=self.estadisticas["fuerza"] * 2
        self.vida_actual=self.vida
        self.mana_actual=self.mana
        self.puntos_de_experiencia=puntos

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Vida: {self.vida}")
        print(f"Mana: {self.mana}")
        print("Estadísticas:")
        for key, value in self.estadisticas.items():
            print(f"  {key}: {value}")
    
    def mostrar_estadisticas(self):
        for key, value in self.estadisticas.items():
            print(f"  {key}: {value}")
    
    def mostrar_nombre(self):
        print(f"Nombre: {self.nombre} | Vida: {self.vida_actual} | Mana: {self.mana_actual}")

    def atacar(self,objetivo):
        self.mostrar_nombre()
        print(f"{self.nombre} ataca a {objetivo.nombre}!")
        objetivo.vida_actual -= self.daño

    def mejorar(self):
        self.mostrar_estadisticas()
        stat=input("que estadisticca quieres mejorar?")
        if stat not in self.estadisticas:
            print("estadistica no valida")
            return
        cantidad=input("cuantos puntos quieres invertir?")
        try:
            cantidad=int(cantidad)
        except ValueError:
            print("cantidad no valida")
            return
        if self.puntos_de_experiencia < cantidad:
            print(f"No tienes suficientes puntos de experiencia para mejorar {stat}.")
            return
        if stat in self.estadisticas:
            self.estadisticas[stat] += cantidad
            print(f"{self.nombre} ha mejorado {stat} en {cantidad} puntos.")
        else:
            print(f"{stat} no es una estadística válida.")