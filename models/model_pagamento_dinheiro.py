from models.model_pagamento import Pagamento


class PagamentoDinheiro(Pagamento):

    def registrar_pagamento(self) -> bool:
        return (
            self.validar_data_pagamento()
            and self.validar_valor_pago()
        )

    def confirmar_pagamento(self) -> bool:
        return self.registrar_pagamento()
