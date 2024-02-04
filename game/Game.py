import random as rd

# DEFINICION DE LA CLASE DE LOS PJ
class Pokimon:
    def __init__(self, nombre, poder_atq, defensa, defensa_e, 
                 nivel, tipo_atq, atq_e, tipo, puntos):

        self.nombre = nombre
        self.poder_atq = poder_atq
        self.atq_e = atq_e
        self.defensa = defensa
        self.defensa_e = defensa_e
        self.tipo_atq = tipo_atq
        self.nivel = nivel
        self.tipo = tipo
        self.vida = 100
        self.turno = 1
        self.puntos = puntos

    def nivel(self, enemigo):

        while self.atacar(enemigo) or enemigo.vida >= 0:
            self.puntos += rd.randint(5,25)

        nivel_siguiente = self.nivel + 1
        puntos_requeridos = nivel_siguiente * (25,65)

        if self.puntos >= puntos_requeridos:
            self.nivel = nivel_siguiente
            self.puntos = 0

        self.vida = self.vida + 15
        self.poder_atq = self.poder_atq + 10
        self.defensa = self.defensa + 5
        self.defensa_e = self.defensa_e + 4


    def atacar(self, enemigo, tipo_atq, tipo):

        Efect = rd.choice([0, 0.25, 0.5, 1, 2, 4])
        Var = rd.randint(85,100)

        bonus = 1
        while self.tipo == enemigo.tipo:
            bonus = 1.5
            break

        if  self.tipo_atq == tipo:
            Defe = enemigo.defensa_e
        elif self.tipo_atq == tipo:
            Defe = enemigo.defensa

        danio = 0.01 * bonus * Efect * Var * (((0.2 * enemigo.nivel+1) * 
                                               enemigo.poder_atq) / 25 * Defe + 2)

    def curarse(self):
        while self.vida < 15:
            self.vida = self.vida + 15
            break

#Clase Pikapija
class Pikapija(Pokimon):
    def __init__(self, nombre, poder_atq, defensa, defensa_e, nivel, tipo_atq, atq_e, tipo, puntos):
        super.__init__(nombre, poder_atq, defensa, defensa_e, nivel, tipo_atq, atq_e, tipo, puntos)
        self.tipo = 'Electrico'
        ataque = "Impackktruenos"
        ataque == self.tipo

def mostrar_estado(Pokimon):
    print(f"{Pokimon.nombre}")
    print(f"{Pokimon.poder_atq}")
    print(f"{Pokimon.defensa}")
    print(f"{Pokimon.defensa_e}")
    print(f"{Pokimon.tipo}")
    print(f"{Pokimon.nivel}")
    print(f"{Pokimon.puntos}")
    print(f"{Pokimon.vida}")

def turno(jugador,enemigo):
    #EL JUGADOR ELIGE SU ACCION
    while jugador.turno == 1:

        print("-------------------")
        mostrar_estado(jugador)
        print("-------------------")

        print("\n")
        accion = int(input("Realiza un movimiento (1-4): "))
        print("\n")

        if accion == 1:
            pass
        elif accion == 2:
            pass
        elif accion == 3:
            pass
        elif accion == 4:
            pass
        else:
            print("Accion no valida")

    print("\n")
    print("-------------------")
    mostrar_estado(enemigo)
    print("-------------------")


#MENU DE ELECCION
def menu_selec():
    print("")
    print("|------------------------------------------------|")
    print("|   ¡ BIENVENIDO A LA FANTASTICA COPIA DE POKI ! |")
    print("|    Ingrese alguna de las siguientes opciones:  |")
    print("|                                                |")
    print("|         1 - Pikapija                           |")
    print("|         2 - Chámame                            |")
    print("|         3 - Propulsor                          |")
    print("|         4 - Skirtgirl                          |")
    print("|------------------------------------------------|\n")
    elec = int(input("Eleccion: "))

    if elec == 1:
        pass
    elif elec == 2:
        pass
    elif elec == 3:
        pass
    elif elec == 4:
        pass
    else:
        print("\nEste Pokimon Aún no existe\n")

    bot = rd.choice(["Pikapija","Chámame","Propulsor","Skirtgirl"])

#MENU PRINCIPAL
def main_menu():
    escape = 2
    while True:
        print("")
        print("|------------------------------------------------|")
        print("|   ¡ BIENVENIDO A LA FANTÁSTICA COPIA DE POKI ! |")
        print("|    Ingrese alguna de las siguientes opciones:  |")
        print("|                                                |")
        print("|         1 - Empezar a Jugar                    |")
        print("|         2 - Salir                              |")
        print("|                                                |")
        print("|------------------------------------------------|\n")
        esc = int(input("Elegir: "))

        if esc == escape:
            print("\n   Juego Terminado\n")
            break
        elif esc != escape:
            menu_selec()

def inicioJuego(jugador,enemigo,turno):
    while True:

        turno(jugador,enemigo)

        if jugador.vida <= 0:
            print(enemigo.nombre," ha ganado\n")
            break
        elif enemigo.vida <= 0:
            print(jugador.nombre," ha ganado\n")
            break
        else:
            print("\nHa habido un Empate\n")

if __name__ == "__main__":
    main_menu()
