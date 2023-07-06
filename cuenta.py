class Cuenta:
    # Lista para almacenar los identificadores de los titulares existentes
    titulares_exist = []
    # Tupla con los tipos de cuenta disponibles
    TIPO_CUENTA = ("Ahorro", "Corriente")

    def __init__(self, id_titular, nombre_titular, num_cuenta, saldo, fecha, tipo_cuenta, cupo):
        #Constructor de la clase cuenta
        self.__id_titular = id_titular
        self.titulares_exist.append(self.__id_titular) if self.__id_titular != None else None
        self.__nombre_titular = nombre_titular
        self.__num_cuenta = num_cuenta
        self.__saldo = saldo
        self.__fecha = fecha
        self.__tipo_cuenta = tipo_cuenta
        self.__cupo = cupo

    def visualizar(self):
        """
        Muestra la información de la cuenta.
        """
        print("Identificacion del titular: " , self.__id_titular)
        print("Nombre del titular: ", self.__nombre_titular)
        print("Numero de cuenta: ", self.__num_cuenta)
        print("Fecha de apertura: ",self.__fecha)
        print("Tipo de cuenta: ", self.__tipo_cuenta)
        print("Saldo de la cuenta: ", self.__saldo)
        print("Cupo de la cuenta: ", self.__cupo if self.__saldo >= 0 else self.__cupo + (self.__saldo))
        print("Total disponibles: ", self.__saldo + self.__cupo)
        
        #Devuelve
    def get_num_cuenta(self):
        return self.__num_cuenta
    
    def get_id_titular(self):
        return self.__id_titular
    
    def get_saldo(self):
        return self.__saldo
    
    def get_nombre_titular(self):
        return self.__nombre_titular
    
    def retirar(self, monto):
        if self.__tipo_cuenta == Cuenta.TIPO_CUENTA[0]:
            if self.__saldo - monto > 0:
                self.__saldo -= monto
                return True
            else:
                return False
        else:
            if (self.__saldo + self.__cupo) - monto > 0 :
                self.__saldo -= monto
                return True
            else:
                return False
            
    def depositar(self, monto):
        if monto > 0 :
            self.__saldo += monto
            return True
        return False            