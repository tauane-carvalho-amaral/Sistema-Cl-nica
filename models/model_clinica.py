from datetime import time

class Clinica:
    def __init__(self, id: int, nome: str, cidade: str, descricao: str, horario_abertura: time, horario_fechamento: time):
        self.__id = id
        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento
      
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
    def cidade(self) -> str:
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str) -> None:
        self.__cidade = cidade
            
    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        self.__descricao = descricao   
        
    @property
    def horario_abertura(self) -> time:
        return self.__horario_abertura

    @horario_abertura.setter
    def horario_abertura(self, horario_abertura: time) -> None:
        self.__horario_abertura = horario_abertura   
        
    @property
    def horario_fechamento(self) -> time:
        return self.__horario_fechamento

    @horario_fechamento.setter
    def horario_fechamento(self, horario_fechamento: time) -> None:
        self.__horario_fechamento = horario_fechamento
        
    
    def validar_horario_funcionamento(self, inicio: time, fim: time) -> bool:
        return (
            self.__horario_abertura <= inicio 
            and fim <= self.__horario_fechamento
        )
