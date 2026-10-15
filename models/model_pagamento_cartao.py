from models.model_pagamento import Pagamento
from models.model_atendimento import Atendimento
from models.model_pessoa_paciente import Paciente
from datetime import date


class PagamentoCartao(Pagamento):
    def __init__(self, id: int, data: date, atendimento: Atendimento, valor_pago: float, paciente: Paciente, numero_cartao: str, bandeira: str):
        super().__init__(id, data, atendimento, valor_pago, paciente)
        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira
    
    @property
    def numero_cartao(self) -> str:
        return self.__numero_cartao

    @property
    def bandeira(self) -> str:
        return self.__bandeira
    
    def confirmar_cartao(self) -> bool:
        return (
            self.validar_data_pagamento()
            and self.validar_valor_pago()
            and bool(self.__numero_cartao.strip())
            and bool(self.__bandeira.strip())
        )
    
    def confirmar_pagamento(self) -> bool:
        return self.confirmar_cartao()
