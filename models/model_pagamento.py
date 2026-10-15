from abc import ABC, abstractmethod
from datetime import date
from models.model_pessoa_paciente import Paciente
from models.model_atendimento import Atendimento



class Pagamento (ABC):
    def __init__(self, id: int, data: date, atendimento: Atendimento, valor_pago: float, paciente: Paciente):
        self.__id = id
        self.__data = data
        self.__atendimento = atendimento
        self.__valor_pago = valor_pago
        self.__paciente = paciente
    
    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id):
        if id is not None and not isinstance(id, int):
            raise TypeError("O ID deve ser inteiro.")
        self.__id = id
    
    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data: date):
        self.__data = data
    
    @property
    def atendimento(self) -> Atendimento:
        return self.__atendimento
    
    @atendimento.setter
    def atendimento(self, atendimento: Atendimento):
        self.__atendimento = atendimento
        
    @property
    def valor_pago(self) -> float:
        return self.__valor_pago
    
    @property
    def valor_total(self) -> float:
        return self.__atendimento.calcular_valor_total()
    
    @property
    def paciente(self) -> Paciente:
        return self.__paciente
    
    @paciente.setter
    def paciente(self, paciente: Paciente):
        self.__paciente = paciente
     
    def calcular_valor_total(self) -> float:
        return self.__atendimento.calcular_valor_total()
      
    def validar_valor_pago(self) -> bool:
        return (
            isinstance(self.__valor_pago, (int, float))
            and not isinstance(self.__valor_pago, bool)
            and self.__valor_pago > 0
        )
    
    def calcular_valor_restante(self) -> float:
        return self.__atendimento.calcular_valor_total() - self.__valor_pago
    
    def validar_data_pagamento(self) -> bool:
        return (
            isinstance(self.__data, date)
            and self.__data <= self.__atendimento.data
        )
    
    @abstractmethod
    def confirmar_pagamento(self) -> bool:
         pass
