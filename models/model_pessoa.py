from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    def __init__(self, id: int, nome: str, cpf: str, data_nascimento: date):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento
        
    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id):
        if id is not None and not isinstance(id, int):
            raise TypeError("O ID deve ser inteiro.")
        self.__id = id
    
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome inválido.")
        self.__nome = nome.strip()
        
    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if not isinstance(cpf, str):
            raise TypeError("CPF deve ser string.")
        self.__cpf = cpf.strip()
        
    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date):
        if not isinstance(data_nascimento, date):
            raise TypeError("A data de nascimento deve ser do tipo datetime.date.")
        self.__data_nascimento = data_nascimento
      
      
    def calcular_idade(self) -> int:
        hoje = date.today()
        idade = hoje.year - self.__data_nascimento.year - (
            (hoje.month, hoje.day) < (self.__data_nascimento.month, self.__data_nascimento.day)
        )
        return idade
    
    def validar_cpf(self) -> bool:
        return len(self.__cpf) == 11 and self.__cpf.isdigit()
    
    @abstractmethod
    def mostrar_dados(self) -> str:
        #Obriga as classes filhas (Paciente e Profissional) a implementarem o Polimorfismo.
        pass