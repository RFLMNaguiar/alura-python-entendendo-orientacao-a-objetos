class Conta:
    # CONSTRUTOR
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular.title()
        self.__saldo = saldo
        self.__limite = limite

    # GETTERS
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    # SETTERS
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # MÉTODOS ESTÁTICOS (de classe)
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001',
                'Caixa': '104',
                'Bradesco': '237',
                'Nu Pagamentos': '260',
                'PicPay': '380'}

    # MÉTODOS DO OBJETO
    def __pode_sacar(self, quantidade):
        if self.__saldo + self.__limite >= quantidade:
            return True
        else:
            return False

    def mostrar_extrato(self):
        print(f"A conta de {self.__titular} possui R${self.__saldo}.")

    def depositar(self, quantidade):
        self.__saldo += quantidade
        print(f"Foram depositados R${quantidade} na conta de {self.__titular}.")
        self.mostrar_extrato()

    def sacar(self, quantidade):
        if self.__pode_sacar(quantidade):
            self.__saldo -= quantidade
            print(f"Foram sacados R${quantidade} na conta de {self.__titular}.")
            self.mostrar_extrato()
        else:
            print(f"Não é possível sacar R${quantidade}. O máximo possível é {self.__saldo + self.__limite}.")

    def transferir(self, quantidade, destino):
        self.sacar(quantidade)
        destino.depositar(quantidade)
        print(f"A quantidade de {quantidade} foi transferida com sucesso de {self.__titular} para {destino.__titular}.")


conta1 = Conta(123, "DANIEL AGUIAR", 100.00, 1000.00)
conta2 = Conta(321, "SAMUEL AGUIAR", 100.00, 2000.00)

conta1.depositar(100)
conta1.transferir(100, conta2)
