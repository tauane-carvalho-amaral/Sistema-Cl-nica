from views.procedimento_view import ProcedimentoView
from models.model_procedimento import Procedimento

class ProcedimentoController:
    # Recebe a lista de profissionais para poder vincular o objeto correto
    def __init__(self, lista_profissionais: list):
        self.__view = ProcedimentoView()
        self.__procedimentos = []
        self.__profissionais = lista_profissionais

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
        
        if any(p.id == dados["id"] for p in self.__procedimentos):
            raise ValueError("Já existe um Procedimento com este ID.")
            
        if not dados["descricao"] or dados["custo"] <= 0:
            raise ValueError("Descrição e custo (maior que zero) são obrigatórios.")

        # Busca o objeto do profissional pelo ID
        prof_obj = next((p for p in self.__profissionais if p.id == dados["id_profissional"]), None)
        if not prof_obj:
            raise ValueError("Profissional não encontrado no sistema.")

        novo_procedimento = Procedimento(
            id=dados["id"],
            descricao=dados["descricao"],
            custo=dados["custo"],
            profissional=prof_obj
        )
        
        # Chama a validação da própria classe conforme o diagrama
        if not novo_procedimento.validar_custo():
            raise ValueError("O custo do procedimento é inválido.")

        self.__procedimentos.append(novo_procedimento)
        self.__view.mostrar_mensagem("Procedimento cadastrado com sucesso!")

    def alterar(self) -> None:
        self.listar()
        self.__view.mostrar_mensagem("Informe o ID que deseja alterar e os novos dados:")
        novos_dados = self.__view.mostrar_dados()
        
        procedimento = next((p for p in self.__procedimentos if p.id == novos_dados["id"]), None)
        if not procedimento:
            raise ValueError("Procedimento não encontrado.")
            
        prof_obj = next((p for p in self.__profissionais if p.id == novos_dados["id_profissional"]), None)
        if not prof_obj:
            raise ValueError("O novo Profissional informado não foi encontrado.")

        procedimento.descricao = novos_dados["descricao"]
        procedimento.custo = novos_dados["custo"]
        procedimento.profissional = prof_obj
        
        if not procedimento.validar_custo():
            raise ValueError("O novo custo do procedimento é inválido.")
            
        self.__view.mostrar_mensagem("Procedimento alterado com sucesso!")

    def excluir(self) -> None:
        self.listar()
        self.__view.mostrar_mensagem("Para EXCLUIR, informe o ID e aperte Enter nos demais campos:")
        dados = self.__view.mostrar_dados()
        
        procedimento = next((p for p in self.__procedimentos if p.id == dados["id"]), None)
        if not procedimento:
            raise ValueError("Procedimento não encontrado.")
            
        self.__procedimentos.remove(procedimento)
        self.__view.mostrar_mensagem("Procedimento excluído com sucesso!")

    def listar(self) -> None:
        if not self.__procedimentos:
            raise ValueError("Nenhum Procedimento cadastrado.")
            
        print("\n--- Lista de Procedimentos ---")
        for p in self.__procedimentos:
            dados_dit = {
                "id": p.id,
                "descricao": p.descricao,
                "custo": p.custo,
                "profissional": p.profissional.nome
            }
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
    def procedimentos(self) -> list:
        return self.__procedimentos