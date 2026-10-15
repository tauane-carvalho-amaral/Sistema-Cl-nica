from datetime import date
from models.model_pessoa import Pessoa

class ProfissionalSaude(Pessoa):
    def __init__(self, id: int, nome: str, cpf: str, data_nascimento: date, especialidade: str, registro_profissional: str):
        super().__init__(id, nome, cpf, data_nascimento)
        
        self.__especialidade = especialidade
        self.__registro_profissional = registro_profissional
        
    @property
    def especialidade(self) -> str:
        return self.__especialidade
    
    @especialidade.setter
    def especialidade(self, especialidade: str):
        if not isinstance(especialidade, str) or not especialidade.strip():
            raise ValueError("Especialidade inválida.")
        self.__especialidade = especialidade.strip()
        
    @property
    def registro_profissional(self) -> str:
        return self.__registro_profissional

    @registro_profissional.setter
    def registro_profissional(self, registro_profissional: str):
        if not isinstance(registro_profissional, str) or not registro_profissional.strip():
            raise ValueError("Registro profissional inválido.")
        self.__registro_profissional = registro_profissional.strip()
        
    def mostrar_dados(self) -> str:
    # Implementação obrigatória devido ao método abstrato na superclasse Pessoa
        return (f"Profissional de Saúde: {self.nome}\nCPF: {self.cpf}\nIdade: {self.calcular_idade()} anos\nEspecialidade: {self.especialidade}\nRegistro Profissional: {self.registro_profissional}")
    