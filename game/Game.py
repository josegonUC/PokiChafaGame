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

        self.vida
        self.poder_atq
        self.defensa
        self.defensa_e


    def atacar(self, enemigo, tipo_atq):

        Efect = rd.choice[0, 0.25, 0.5, 1, 2, 4]
        Var = rd.randint(85,100)

        bonus = 1
        while self.tipo == enemigo.tipo:
            bonus = 1.5
            break

        if  self.tipo_atq == "especial":
            Defe = enemigo.defensa_e
        elif self.tipo_atq == "fisico":
            Defe = enemigo.defensa

        danio = 0.01 * bonus * Efect * Var * (((0.2 * enemigo.nivel+1) * 
                                               enemigo.poder_atq) / 25 * Defe + 2)

    def curarse(self):
        while self.vida < 15:
            self.vida = self.vida + 15
            break

#Clase Pikapija
class Pikapija(Pokimon):
    d




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

    bot = rd.choice()

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


if __name__ == "__main__":
    main_menu()