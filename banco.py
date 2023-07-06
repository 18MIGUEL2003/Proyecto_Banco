from os import system
from datetime import datetime
import random
from cuenta import Cuenta

class Banco:
    """
    Clase que representa el banco y gestiona las cuentas de los clientes.
    """
    def __init__(self):
        """
        Inicializa una instancia de la clase Banco.
        """
        self.__cuentas = []
        self.__numero_cuenta = []
       
    def generar_numero_cuenta(self):
        """
        Genera un número de cuenta único y lo devuelve.
        """
        while True:
            numero = random.randint(1, 9)
            if numero not in self.__numero_cuenta:
                self.__numero_cuenta.append(numero)
                break
        return numero
    
    def buscar_cuenta(self, num_cuenta):
        """
        Busca una cuenta en la lista de cuentas del banco según su número de cuenta.
        Devuelve la posición de la cuenta si se encuentra, o -1 si no se encuentra.
        """
        for i in range(len(self.__cuentas)):
            if self.__cuentas[i].get_num_cuenta() == num_cuenta:
                return i
        return -1

    def buscar_id_titular(self,id_titular):
        """
        Busca si existe una cuenta en la lista de cuentas del banco asociada a un titular específico.
        Devuelve True si se encuentra, o False si no se encuentra.
        """
        for i in range(len(self.__cuentas)):
            if self.__cuentas[i].get_id_titular()==id_titular:
                return True
        return False
    
    def adicionar_cuenta(self, cuenta):
        """
        Agrega una cuenta a la lista de cuentas del banco.
        Devuelve True si se agrega correctamente, o False si la cuenta ya existe.
        """
        pos_cuenta = self.buscar_cuenta(cuenta.get_num_cuenta())
        if pos_cuenta == -1:
         self.__cuentas.append(cuenta)
        return True
    system('cls')
    print('Cuenta ya existente')
    input()

    def visualizar_cuenta(self, num_cuenta):
        """
        Muestra la información de una cuenta específica según su número de cuenta.
        Devuelve True si se encuentra y muestra la información, o False si no se encuentra.
        """
        pos = self.buscar_cuenta(num_cuenta)
        if pos != -1:
            if self.__cuentas[pos].visualizar():
                return True
            return False
    
    def retirar_monto_cuenta(self, num_cuenta, monto):
        """
        Realiza un retiro de la cuenta específica según su número de cuenta y el monto deseado.
        Devuelve True si se realiza el retiro correctamente, o False si no se puede realizar.
        """
        pos = self.buscar_cuenta(num_cuenta)
        if pos != -1:
            if self.__cuentas[pos].retirar(monto):
                return True
        return False
    
    def depositar_monto_cuenta(self,  monto, num_cuenta):
        """
        Realiza un depósito en la cuenta específica según su número de cuenta y el monto deseado.
        Devuelve True si se realiza el depósito correctamente, o False si no se puede realizar.
        """
        pos = self.buscar_cuenta(num_cuenta)
        if pos != -1:
            if self.__cuentas[pos].depositar(monto):
                return True
            return False     
    
    def consular_saldo_cuenta(self, num_cuenta):
        """
        Consulta el saldo de una cuenta específica según su número de cuenta.
        Devuelve el saldo de la cuenta si se encuentra, o None si no se encuentra.
        """
        pos = self.buscar_cuenta(num_cuenta)
        if pos != -1:
            valor = self.__cuentas[pos].get_saldo()
            return valor
    
    def visualizar_cliente(self, num_cuenta):
        """
        Muestra el nombre del titular de una cuenta específica según su número de cuenta.
        Devuelve el nombre del titular si se encuentra, o None si no se encuentra.
        """
        pos = self.buscar_cuenta(num_cuenta)
        if pos != -1:
            valor = self.__cuentas[pos].get_nombre_titular()
            return valor
      
    def pedir_datos_cuenta(self):
        """
        Solicita al usuario los datos para crear una cuenta y la agrega al banco.
        """
        system("cls")
        print("*******************")
        print("**** CREAR CUENTA ****")
        print("*******************")
        id_titular = input("Digite el numero de documento del titular: ")
        if self.buscar_id_titular(id_titular):
            print("Este numero de id ya existe")
            input()
            return 0
        nombre_titular = input("Digite el nombre de titular: ")
        num_cuenta = self.generar_numero_cuenta()
        saldo = int(input("Digite el saldo inicial: "))
        fecha = datetime.now()
       
        while True:
            print("*******************")
            print("**** TIPO DE CUENTA ****")
            print("*******************")
            print("1. Ahorros")
            print("2. Corriente")
            print("*******************")
           
            try:
                op_tipo_cuenta = int(input("Seleccione el tipo de cuenta: "))
               
                if op_tipo_cuenta == 1:
                    tipo_cuenta = "Ahorro"
                    cupo = 0
                    break
               
                elif op_tipo_cuenta == 2:
                    tipo_cuenta = "Corriente"
                   
                    try:
                        cupo = float(input("Digite el cupo que tiene asignado a la cuenta: "))
                        break
                   
                    except ValueError:
                        print("*******************")
                        print("ERROR - El dato debe de ser decimal")
                        print("*******************")
                        input()
                else:
                    print("*******************")
                    print("ERROR - Opcion no valida")
                    print("*******************")
                    input()
               
            except ValueError:
                print("*******************")
                print("ERROR - El dato debe de ser entero")
                print("*******************")
                input()
        
        cuenta = Cuenta(id_titular, nombre_titular, num_cuenta, saldo, fecha, tipo_cuenta, cupo)
       
        if self.adicionar_cuenta(cuenta):
            print("*******************")
            print("INFO - La cuenta se creo correctamente")
            print("El numero de cuenta es: ", num_cuenta)
            print("*******************")
            input()
           
        else:
            print("*******************")
            print("ERROR - La cuenta no se puede crear")
            print("*******************")
            input()
            
    def pedir_datos_visualizar_cuenta(self):
        """
        Solicita al usuario el número de cuenta para visualizar sus datos.
        """
        system("cls")
        print("*******************")
        print("***** VISUALIZAR CUENTA ******")
        print("*******************")
        num_cuenta = int(input("Ingrese el numero de cuenta a visualizar: "))
        
        pos_cuenta = self.buscar_cuenta(num_cuenta)
        
        if pos_cuenta != -1:
            self.visualizar_cuenta(num_cuenta)
            input()
        
    def pedir_datos_retiro_cuenta(self):
        """
        Solicita al usuario el número de cuenta y el monto a retirar de la cuenta.
        Realiza la operación de retiro si es posible.
        """
        system("cls")
        print("*******************")
        print("***** RETIROS ******")
        print("*******************")
        num_cuenta = int(input("Ingrese el numero de la cuenta: "))
        
        if self.buscar_cuenta(num_cuenta) !=-1:
            monto = float(input("Ingrese el monto a retirar: "))
            
            if self.retirar_monto_cuenta(num_cuenta, monto):
            
                print("*******************")
                print("Info - El retiro se realizo")
                print("*******************")
                input()
                
            else:
               
                print("*******************")
                print("Error - el retiro no se puede realizar")
                print("*******************")    
                input()
                
        else:
            print("*******************")
            print("El numero de la cuenta no existe")
            print("*******************")          
            
    def pedir_datos_deposito_cuenta(self):
        """
        Solicita al usuario el número de cuenta y el monto a depositar en la cuenta.
        Realiza la operación de depósito si es posible.
        """
        system("cls")
        print("*******************")
        print("*** DEPOSITO ***")
        print("*******************")            
        num_cuenta = int(input("Digite el numero de cuenta: "))
        
        if self.buscar_cuenta(num_cuenta)!= -1:
            monto = float(input("Ingrese el monto a depositar: "))
            
            if self.depositar_monto_cuenta(monto, num_cuenta):
                print("*******************")
                print("Info - El deposito fue realizado")
                print("*******************")   
                input()    
            else:    
                print("*******************")
                print("Error - El deposito no se puede realizar")
                print("*******************") 
                input()
                
        else:
            print("*******************")
            print("Error - El numero de cuenta no existe")
            print("*******************")                 
            input()
    
    def mostrar_saldo_cuenta(self):
        """
        Solicita al usuario el número de cuenta para mostrar su saldo.
        """
        system("cls")
        print("*******************")
        print("*** Mostrar saldo ***")
        print("*******************")  
        num_cuenta = int(input("Ingrese el numero de la cuenta: "))
        
        if self.buscar_cuenta(num_cuenta) != -1:
            print("*******************")
            print("Info- El saldo de su cuenta es: ", (self.consular_saldo_cuenta(num_cuenta)))
            print("*******************")                 
            input()
       
        else:
            print("*******************")
            print("Error- El nuero de cuenta no existe: ")
            print("*******************")                 
            input()
            
    def pedir_datos_visualiar_cliente(self):
        """
        Solicita al usuario el número de cuenta para mostrar el nombre del titular.
        """
        system("cls")
        print("*******************")
        print("*** Mostrar cliente***")
        print("*******************")  
        num_cuenta = int(input("Digite el numero de la cuenta: "))
        
        
        if self.buscar_cuenta(num_cuenta) != -1:
            print("*******************")
            print("Info- El nombre del cliente es: ", (self.visualizar_cliente(num_cuenta)))
            print("*******************")                 
            input()
       
        else:
            print("*******************")
            print("Error- El numero de cuenta no existe: ")
            print("*******************")                 
            input()