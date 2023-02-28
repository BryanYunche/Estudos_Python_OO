"""
Lançamos o seguinte desafio: para ajudar na formatação de datas você deve criar uma nova classe auxiliar.
Essa classe deve representar uma Data (sem hora) que sabe imprimir uma data formatada.
"""

class Data:
    def __init__(self, dia = "27", mes = "02", ano = "2023"):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        return print(f'{self.dia}/{self.mes}/{self.ano}')
