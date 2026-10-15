from views.sistema_view import SistemaView
from controllers.clinica_controller import ClinicaController
from controllers.pessoa_controller import PessoaController
from controllers.tipo_atendimento_controller import TipoAtendimentoController
from controllers.atendimento_controller import AtendimentoController
from controllers.procedimento_controller import ProcedimentoController
from controllers.pagamento_controller import PagamentoController
from controllers.relatorio_controller import RelatorioController
import sys

class SistemaController:
    def __init__(self):
        self.__view_sistema = SistemaView()
        
        self.__ctrl_clinica = ClinicaController()
        self.__ctrl_pessoa = PessoaController()
        self.__ctrl_tipo_atendimento = TipoAtendimentoController()
        
        self.__ctrl_procedimento = ProcedimentoController(self.__ctrl_pessoa.profissionais)
        
        self.__ctrl_atendimento = AtendimentoController(
            self.__ctrl_clinica.clinicas,
            self.__ctrl_pessoa.pacientes,
            self.__ctrl_pessoa.profissionais,
            self.__ctrl_tipo_atendimento.tipos,
            self.__ctrl_procedimento.procedimentos
        )
        
        self.__ctrl_pagamento = PagamentoController(self.__ctrl_atendimento.atendimentos)
        
        self.__ctrl_relatorio = RelatorioController(
            self.__ctrl_atendimento,
            self.__ctrl_clinica,
            self.__ctrl_procedimento
        )
        
    def iniciar(self) -> None:
        opcoes = {
            1: self.__ctrl_clinica.abrir_menu,
            2: self.__ctrl_pessoa.abrir_menu,
            3: self.__ctrl_tipo_atendimento.abrir_menu,
            4: self.__ctrl_atendimento.abrir_menu,
            5: self.__ctrl_procedimento.abrir_menu,
            6: self.__ctrl_pagamento.abrir_menu,
            7: self.__ctrl_relatorio.abrir_menu,
            0: self.encerrar_sistema
        }
        
        while True:
            try:
                opcao = self.__view_sistema.mostrar_menu()
                funcao = opcoes.get(opcao)
                if funcao:
                    funcao()
                else:
                    self.__view_sistema.exibir_erro("Opção inválida! Tente novamente.")
            except Exception as e:
                self.__view_sistema.exibir_erro(f"Erro inesperado: {e}")

    def encerrar_sistema(self) -> None:
        self.__view_sistema.mostrar_mensagem("Sistema encerrado com sucesso.")
        sys.exit(0)
