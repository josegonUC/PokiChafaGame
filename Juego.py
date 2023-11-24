import random

#DEFINICION DE LAS CLASES DE POKIMON
class Pokimon:
    def __init__(self, nombre, fuerza, defensa):
        self.nombre = nombre
        self.fuerza = fuerza
        self.defensa = defensa
        self.vida = 100
        self.turno = 1

    def atacar(self, enemigo,tipo_atq):
        if tipo_atq == 'Basico':
            danio = round((self.fuerza - enemigo.defensa) / 3.5)
        elif tipo_atq == 'Cargado':
            danio = round((self.fuerza - enemigo.defensa) / 2)
        elif tipo_atq == 'Especial':
            danio = round((self.fuerza - enemigo.defensa) / 1.5)
        else:
            danio = 0
        enemigo.vida = enemigo.vida - danio

    def curarse(self):
        if self.vida < 100:
            self.vida = self.vida + 15

#DEFINICION DE LAS FUNCIONES DEL JUEGO
def mostrar_estado(Pokimon):
    print(f"Nombre: {Pokimon.nombre}")
    print(f"Fuerza: {Pokimon.fuerza}")
    print(f"Defensa: {Pokimon.defensa}")
    print(f"Vida: {Pokimon.vida}")

def turno(jugador, enemigo):
    #EL JUGADOR ELIGE SU ACCION
    while jugador.turno == 1:
        
        print("-------------------")
        mostrar_estado(jugador)
        print("-------------------")
        
        print("\n")
        accion = int(input("¿Que deseas Hacer? (1-4): "))
        print("\n")

        if accion == 1:
            jugador.atacar(enemigo, "Basico")
            print("+++++++++++++++++++++++++++++++++++")
            print(f"{jugador.nombre} ha usado Ataque Basico")
            print("+++++++++++++++++++++++++++++++++++")
        elif accion == 2:
            jugador.atacar(enemigo, "Cargado")
            print("+++++++++++++++++++++++++++++++++++")
            print(f"\n{jugador.nombre} ha usado Ataque Cargado")
            print("+++++++++++++++++++++++++++++++++++")
        elif accion == 3:
            jugador.atacar(enemigo, "Especial")
            print("+++++++++++++++++++++++++++++++++++")
            print(f"{jugador.nombre} ha usado Ataque Especial")
            print("+++++++++++++++++++++++++++++++++++")
        elif accion == 4:
            jugador.curarse()
            print("+++++++++++++++++++++++++++++++++++")
            print(f"{jugador.nombre} se ha Curado")
            print("+++++++++++++++++++++++++++++++++++")
        else:
            print("Accion no valida")

        jugador.turno = jugador.turno - 1
    
    print("\n")
    print("-------------------")
    mostrar_estado(enemigo)
    print("-------------------")

    #EL ENEMIGO ELIGE SU ACCION ALEATORIAMENTE
    tipo_atq = random.choice(["Basico", "Cargado", "Especial"])
    enemigo.atacar(jugador, tipo_atq)
    print("+++++++++++++++++++++++++++++++++++++++")
    print(f"{enemigo.nombre} ha usado Ataque {tipo_atq}")
    print("+++++++++++++++++++++++++++++++++++++++")
    if enemigo.vida < 20:
        enemigo.curarse()
        print("+++++++++++++++++++++++++++++++++++++++")
        print(f"{enemigo.nombre} se ha curado")
        print("+++++++++++++++++++++++++++++++")

    jugador.turno = jugador.turno + 1

#INICIO DEL JUEGO
jugador = Pokimon("Pikapija", 100,50)
enemigo = Pokimon("Propulsor", 85,60)

while True:

    turno(jugador, enemigo)

    if jugador.vida <= 0:
        print(enemigo.nombre," Ha ganado\n")
        break
    elif enemigo.vida <= 0:
        print(jugador.nombre," Ha Ganado\n")
        break
    elif jugador.vida <= 0 and enemigo.vida <= 0:
        print("\nHa habido un empate\n")
        break


