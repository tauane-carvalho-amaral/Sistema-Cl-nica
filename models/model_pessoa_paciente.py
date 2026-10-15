from datetime import date
from models.model_pessoa import Pessoa


class Paciente(Pessoa):
    def __init__(self, id: int, nome: str, cpf: str, data_nascimento: date):
        super().__init__(id, nome, cpf, data_nascimento)
        
    def eh_maior_de_idade(self) -> bool:
        return self.calcular_idade() >= 18    
    
    def validar_atendimento_independente(self) -> bool:
        return self.eh_maior_de_idade()
    
    def mostrar_dados(self) -> str:
    # Implementação obrigatória devido ao método abstrato na superclasse Pessoa
        return f"Paciente: {self.nome}\nCPF: {self.cpf}\nIdade: {self.calcular_idade()} anos"
