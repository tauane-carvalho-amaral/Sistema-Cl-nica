from datetime import date, time
from models.model_clinica import Clinica
from models.model_pessoa_paciente import Paciente
from models.model_pessoa_profissional_saude import ProfissionalSaude
from models.model_tipo_atendimento import TipoAtendimento
from models.model_procedimento import Procedimento

class Atendimento:
    def __init__(self, id: int, clinica: Clinica, paciente: Paciente, profissional: ProfissionalSaude, data: date, horario_inicio: time, horario_fim: time, tipo_atendimento: TipoAtendimento, procedimentos: list[Procedimento], valor_total: float):
        self.__id = id
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__tipo_atendimento = tipo_atendimento
        self.__procedimentos = procedimentos
        self.__valor_total = valor_total
    
    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id):
        if id is not None and not isinstance(id, int):
            raise TypeError("O ID deve ser inteiro.")
        self.__id = id
    
    @property
    def clinica(self) -> Clinica:
        return self.__clinica
    
    @clinica.setter
    def clinica(self, clinica: Clinica):
        self.__clinica = clinica
        
    @property
    def paciente(self) -> Paciente:
        return self.__paciente
    
    @paciente.setter
    def paciente(self, paciente: Paciente):
        self.__paciente = paciente
        
    @property
    def profissional(self) -> ProfissionalSaude:
        return self.__profissional
    
    @profissional.setter
    def profissional(self, profissional: ProfissionalSaude):
        self.__profissional = profissional
        
    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data: date):
        self.__data = data
        
    @property
    def horario_inicio(self) -> time:
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio: time):
        self.__horario_inicio = horario_inicio   
        
    @property
    def horario_fim(self) -> time:
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim: time):
        self.__horario_fim = horario_fim
        
    @property
    def tipo_atendimento(self) -> TipoAtendimento:
        return self.__tipo_atendimento

    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento: TipoAtendimento):
        self.__tipo_atendimento = tipo_atendimento

    @property
    def valor_total(self) -> float:
        return self.__valor_total
    
    #adiciona um procedimento
    def add_procedimento(self, procedimento: Procedimento) -> None:
        if procedimento not in self.__procedimentos:
            self.__procedimentos.append(procedimento)
            self.calcular_valor_total()
    
    #remove um procedimento
    def rem_procedimento(self, procedimento: Procedimento) -> None:
        if procedimento in self.__procedimentos:
            self.__procedimentos.remove(procedimento)
            self.calcular_valor_total()
            
    #calcula o valor total dos procedimentos
    def calcular_valor_total(self) -> float:
        self.__valor_total = sum(
            procedimento.custo
            for procedimento in self.__procedimentos
        )
        return self.__valor_total
    
    #valida as regras do agendamento
    def validar_regras_agendamento(self) -> None:
        if self.__data is None:
            raise ValueError('A data do atendimento é obrigatoria!!')
        
        if self.__horario_inicio >= self.__horario_fim:
            raise ValueError('O horário de início deve ser anterior ao horário de fim.')
        
        if self.__paciente is None:
            raise ValueError('O atendimento deve possuir um paciente.')
        
        if self.__profissional is None:
            raise ValueError('O atendimento deve possuir um profissional.')

        # Regra 1: Validação de maioridade do paciente
        if not self.__paciente.validar_atendimento_independente():
            raise ValueError('Paciente menor de idade não pode realizar atendimento independente.')
        
        # Regra 2: Validação de horário de funcionamento da clínica
        if not self.__clinica.validar_horario_funcionamento(self.__horario_inicio, self.__horario_fim):
            raise ValueError('O horário do atendimento está fora do funcionamento da clínica.')

    @property
    def procedimentos(self) -> list:
        return self.__procedimentos
