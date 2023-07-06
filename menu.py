from banco import Banco
from os import system
class menu:
    """
    Clase que representa el menú principal del sistema bancario.
    """

    def mostrar_menu_pricipal(self):
        """
        Método para mostrar y gestionar el menú principal.
        """
        while True:
            system("cls")
            print("*******************")
            print("*******************")
            print("***** BANCO ******")
            print("*******************")
            print("1. Crear Cuenta")
            print("2: Visualizar Cuenta")
            print("3: Retiro")
            print("4: Deposito")
            print("5: Consultar saldo")
            print("6: Consultar cliente")
            print("0. Salir")
            print("*******************")
           
            try:
                opcion = int(input("Ingrese la opcion: "))
                print("*******************")
               
                if opcion == 1:
                    banco.pedir_datos_cuenta()
                    
                elif opcion == 2:
                    banco.pedir_datos_visualizar_cuenta()  
                    
                elif opcion == 3:
                    banco.pedir_datos_retiro_cuenta()   
                 
                elif opcion == 4:
                    banco.pedir_datos_deposito_cuenta() 
                    
                elif opcion == 5:
                    banco.mostrar_saldo_cuenta()   
                    
                elif opcion == 6:
                    banco.pedir_datos_visualiar_cliente()                 
                   
                elif opcion == 0:
                    break
               
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
               
if __name__ == "__main__":
    banco = Banco()
    menu = menu()
    menu.mostrar_menu_pricipal()