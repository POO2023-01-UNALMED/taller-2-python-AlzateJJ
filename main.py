class Asiento:
    def __init__(self, color, precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro

    def cambiarColor(self, color):
        colores= ["rojo", "verde", "amarillo", "negro", "blanco"]
        for c in colores:
            if color == c:
                self.color=color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro(self, registro):
        self.registro=registro

    def asignarTipo(self, tipo):
        if tipo=="gasolina" or tipo=="electrico":
            self.tipo=tipo

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
        self.cantidadCreados=cantidadCreados


    def cantidadAsientos(self):
        numAsientos=0
        for a in self.asientos:
            if type(a)==Asiento:
                numAsientos+=1
        return numAsientos

    def verificarIntegridad(self):
        if (self.registro==self.motor.registro):
            for a in self.asientos:
                if type(a)==Asiento:
                    if a.registro!=self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"

