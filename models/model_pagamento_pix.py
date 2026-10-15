from models.model_pagamento import Pagamento
from models.model_atendimento import Atendimento
from models.model_pessoa_paciente import Paciente
from datetime import date


class PagamentoPix(Pagamento):
    def __init__(self, id: int, data: date, atendimento: Atendimento, valor_pago: float, paciente: Paciente, cpf_pagador: str):
        super().__init__(id, data, atendimento, valor_pago, paciente)
        self.__cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self) -> str:
        return self.__cpf_pagador

    def confirmar_pix(self) -> bool:
        return (
            self.validar_data_pagamento()
            and self.validar_valor_pago()
            and bool(self.__cpf_pagador.strip())
        )

    def confirmar_pagamento(self) -> bool:
        return self.confirmar_pix()
