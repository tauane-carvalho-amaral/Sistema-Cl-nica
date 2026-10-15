from views.tipo_atendimento_view import TipoAtendimentoView
from models.model_tipo_atendimento import TipoAtendimento

class TipoAtendimentoController:
    def __init__(self):
        self.__view = TipoAtendimentoView()
        self.__tipos_atendimento = []

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
                self.__view.exibir_erro("Opção inválida selecionada.")

    def incluir(self) -> None:
        dados = self.__view.mostrar_dados()
        
        if any(t.id == dados["id"] for t in self.__tipos_atendimento):
            raise ValueError("Já existe um Tipo de Atendimento com este ID.")
            
        if not dados["nome"]:
            raise ValueError("O nome do Tipo de Atendimento é obrigatório.")
            
        novo_tipo = TipoAtendimento(
            id=dados["id"],
            nome=dados["nome"],
            descricao=dados["descricao"]
        )
        self.__tipos_atendimento.append(novo_tipo)
        self.__view.mostrar_mensagem("Tipo de Atendimento cadastrado com sucesso!")

    def alterar(self) -> None:
        self.listar()
        self.__view.mostrar_mensagem("Informe o ID que deseja alterar e os novos dados:")
        novos_dados = self.__view.mostrar_dados()
        
        tipo = next((t for t in self.__tipos_atendimento if t.id == novos_dados["id"]), None)
        if not tipo:
            raise ValueError("Tipo de Atendimento não encontrado no sistema.")
            
        if not novos_dados["nome"]:
            raise ValueError("O nome não pode ficar vazio na alteração.")
            
        tipo.nome = novos_dados["nome"]
        tipo.descricao = novos_dados["descricao"]
        
        self.__view.mostrar_mensagem("Tipo de Atendimento alterado com sucesso!")

    def excluir(self) -> None:
        self.listar()
        self.__view.mostrar_mensagem("Para EXCLUIR, informe o ID e aperte Enter nos demais campos:")
        dados = self.__view.mostrar_dados()
        
        tipo = next((t for t in self.__tipos_atendimento if t.id == dados["id"]), None)
        if not tipo:
            raise ValueError("Tipo de Atendimento não encontrado.")
            
        self.__tipos_atendimento.remove(tipo)
        self.__view.mostrar_mensagem("Tipo de Atendimento excluído com sucesso!")

    def listar(self) -> None:
        if not self.__tipos_atendimento:
            raise ValueError("Nenhum Tipo de Atendimento cadastrado no sistema.")
            
        print("\n--- Lista de Tipos de Atendimento ---")
        for tipo in self.__tipos_atendimento:
            dados_dit = {
                "id": tipo.id,
                "nome": tipo.nome,
                "descricao": tipo.descricao
            }
            self.__view.mostrar_lista(dados_dit)

    def tratar_excecoes(self, funcao_metodo) -> None:
        try:
            funcao_metodo()
        except ValueError as e:
            self.__view.exibir_erro(f"Erro de Validação/Dados: {e}")
        except TypeError as e:
            self.__view.exibir_erro(f"Erro de Tipagem: {e}")
        except Exception as e:
            self.__view.exibir_erro(f"Falha Crítica Inesperada: {e}")

    # Getter essencial para injetar a lista no AtendimentoController
    @property
    def tipos(self) -> list:
        return self.__tipos_atendimento