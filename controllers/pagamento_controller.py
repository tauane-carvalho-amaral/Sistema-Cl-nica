from views.pagamento_view import PagamentoView
from models.model_pagamento_dinheiro import PagamentoDinheiro
from models.model_pagamento_pix import PagamentoPix
from models.model_pagamento_cartao import PagamentoCartao
from datetime import datetime

class PagamentoController:
    # Recebe a lista de atendimentos para poder vincular o pagamento ao atendimento correto
    def __init__(self, lista_atendimentos: list):
        self.__view = PagamentoView()
        self.__pagamentos = []
        self.__atendimentos = lista_atendimentos

    def abrir_menu(self) -> None:
        opcoes = {
            1: self.incluir,
            2: self.alterar,
            3: self.excluir,
            4: self.listar
        }
        while True:
            opcao = self.__view.mostrar_menu()
            if opcao == 0:
                break
            elif opcao in opcoes:
                self.tratar_excecoes(opcoes[opcao])
            else:
                self.__view.exibir_erro("Opção inválida.")

    def incluir(self) -> None:
        dados = self.__view.mostrar_dados()
        
        if any(p.id == dados["id"] for p in self.__pagamentos):
            raise ValueError("Já existe um Pagamento registado com este ID.")
            
        if dados["valor"] <= 0:
            raise ValueError("O valor do pagamento deve ser maior que zero.")

        # 1. Procurar o Atendimento vinculado
        atendimento = next((a for a in self.__atendimentos if a.id == dados["id_atendimento"]), None)
        if not atendimento:
            raise ValueError("Atendimento não encontrado no sistema.")

        data_pagamento_obj = datetime.strptime(dados["data"], "%d/%m/%Y").date()
        
        # Regra 3 do PDF: "Os pagamentos devem ser realizados até a data do atendimento"
        if data_pagamento_obj > atendimento.data:
            raise ValueError("A data do pagamento não pode ser posterior à data do atendimento.")

        # 2. Instanciar a classe filha correta
        novo_pagamento = None
        if dados["tipo"] == '1':
            novo_pagamento = PagamentoDinheiro(
                id=dados["id"], data=data_pagamento_obj, atendimento=atendimento,
                valor_pago=dados["valor"], paciente=atendimento.paciente
            )
        elif dados["tipo"] == '2':
            if not dados.get("cpf_pagador"):
                raise ValueError("CPF do pagador é obrigatório para pagamentos via PIX.")
            novo_pagamento = PagamentoPix(
                id=dados["id"], data=data_pagamento_obj, atendimento=atendimento,
                valor_pago=dados["valor"], paciente=atendimento.paciente,
                cpf_pagador=dados["cpf_pagador"]
            )
        elif dados["tipo"] == '3':
            if not dados.get("numero_cartao") or not dados.get("bandeira"):
                raise ValueError("Número e bandeira do cartão são obrigatórios.")
            novo_pagamento = PagamentoCartao(
                id=dados["id"], data=data_pagamento_obj, atendimento=atendimento,
                valor_pago=dados["valor"], paciente=atendimento.paciente,
                numero_cartao=dados["numero_cartao"], bandeira=dados["bandeira"]
            )
        else:
            raise ValueError("Tipo de pagamento inválido.")

        # Adiciona à lista
        self.__pagamentos.append(novo_pagamento)
        self.__view.mostrar_mensagem(f"Pagamento registado! Valor restante do atendimento: R$ {novo_pagamento.calcular_valor_restante():.2f}")

    def alterar(self) -> None:
        # A lógica de alteração segue os mesmos princípios. Para manter o MVC e encapsulamento,
        # geralmente exclui-se o pagamento errado e insere-se um novo.
        self.__view.exibir_erro("Por questões de auditoria financeira, pagamentos não devem ser alterados. Exclua o registo incorreto e insira um novo.")

    def excluir(self) -> None:
        self.listar()
        self.__view.mostrar_mensagem("Para EXCLUIR, informe o ID (carregue em Enter nos restantes):")
        dados = self.__view.mostrar_dados()
        
        pagamento = next((p for p in self.__pagamentos if p.id == dados["id"]), None)
        if not pagamento:
            raise ValueError("Pagamento não encontrado.")
            
        self.__pagamentos.remove(pagamento)
        self.__view.mostrar_mensagem("Pagamento excluído com sucesso!")

    def listar(self) -> None:
        if not self.__pagamentos:
            raise ValueError("Nenhum pagamento registado no sistema.")
            
        print("\n--- Lista de Pagamentos ---")
        for p in self.__pagamentos:
            dados_dit = {
                "id": p.id,
                "id_atendimento": p.atendimento.id,
                "data": p.data.strftime("%d/%m/%Y"),
                "valor": p.valor_pago,
                "valor_restante": p.calcular_valor_restante()
            }
            
            if isinstance(p, PagamentoDinheiro):
                dados_dit["modalidade"] = "Dinheiro"
                dados_dit["detalhes"] = ""
            elif isinstance(p, PagamentoPix):
                dados_dit["modalidade"] = "PIX"
                dados_dit["detalhes"] = f"CPF: {p.cpf_pagador}"
            elif isinstance(p, PagamentoCartao):
                dados_dit["modalidade"] = "Cartão de Crédito"
                dados_dit["detalhes"] = f"Cartão: {p.numero_cartao} ({p.bandeira})"
                
            self.__view.mostrar_lista(dados_dit)

    def tratar_excecoes(self, funcao_metodo) -> None:
        try:
            funcao_metodo()
        except ValueError as e:
            self.__view.exibir_erro(f"Erro de Validação: {e}")
        except TypeError as e:
            self.__view.exibir_erro(f"Erro de Tipagem: {e}")
        except Exception as e:
            self.__view.exibir_erro(f"Erro Inesperado: {e}")

    @property
    def pagamentos(self) -> list:
        return self.__pagamentos
