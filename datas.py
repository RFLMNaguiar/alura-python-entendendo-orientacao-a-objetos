class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatar_data_brasileira(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")

    def formatar_data_americana(self):
        print(f"{self.mes}/{self.dia}/{self.ano}")


d = Data(10, 7, 1999)
