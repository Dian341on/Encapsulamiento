"""Crea una clase llamada CuentaBancaria que tenga atributos como titular,
saldo y numero_cuenta. Implementa métodos para depositar y retirar dinero, 
asegurándote de que el saldo no se vuelva negativo"""

class CuentaBancaria:
    def __init__ (self, titular, saldo, numero_cuenta): 
        self.titular = titular
        self.saldo = 0.0 
        self.numero_cuenta = numero_cuenta
        
    def depositar_plata (self, saldo):
        self.saldo = saldo + deposito
        return self.saldo
    
    def retirar_plata (self, saldo):
        self.saldo = saldo - retiro 
        if self.saldo < 0.0 : 
            print ("No puede hacer hacer ese retiro")
        else: 
            return self.saldo
