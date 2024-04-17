class Conta_bancária:
    def __init__(self, numero_da_conta, saldo, titular):
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo 
        self.titular = titular
    if __name__ == "__main__":
        conta1 = any("12345678", "R$100", "Thiago")  
        conta2 = any("345678", "R$2000", "Isabelly")
        print(conta1.numero_da_conta, conta1.saldo, conta1.titular)
        print(conta2.numero_da_conta, conta2.saldo, conta2.titular)