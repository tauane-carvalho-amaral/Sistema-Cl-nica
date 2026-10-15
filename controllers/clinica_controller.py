from views.clinica_view import ClinicaView
from models.model_clinica import Clinica
from datetime import datetime

class ClinicaController:
    def __init__(self):
        self.__view = ClinicaView()
        self.__clinicas = []

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
        
        if any(c.id == dados["id"] for c in self.__clinicas):
            raise ValueError("Já existe uma clínica cadastrada com este ID.")
        
        if not dados["nome"] or not dados["horario_abertura"]:
            raise ValueError("Nome e horários são obrigatórios para incluir.")
        
        abertura = datetime.strptime(dados["horario_abertura"], "%H:%M").time()
        fechamento = datetime.strptime(dados["horario_fechamento"], "%H:%M").time()
        
        nova_clinica = Clinica(
            id=dados["id"], 
            nome=dados["nome"], 
            cidade=dados["cidade"], 
            descricao=dados["descricao"], 
            horario_abertura=abertura, 
            horario_fechamento=fechamento
        )
        self.__clinicas.append(nova_clinica)
        self.__view.mostrar_mensagem("Clínica cadastrada com sucesso!")

    def alterar(self) -> None:
        self.listar()
        self.__view.mostrar_mensagem("Informe o ID da Clínica que deseja alterar e os novos dados:")
        novos_dados = self.__view.mostrar_dados()
        
        clinica = next((c for c in self.__clinicas if c.id == novos_dados["id"]), None)
        if not clinica:
            raise ValueError("Clínica não encontrada no sistema.")
        
        if not novos_dados["nome"] or not novos_dados["horario_abertura"]:
            raise ValueError("Os novos dados (nome e horários) não podem ficar vazios na alteração.")
        
        clinica.nome = novos_dados["nome"]
        clinica.cidade = novos_dados["cidade"]
        clinica.descricao = novos_dados["descricao"]
        clinica.horario_abertura = datetime.strptime(novos_dados["horario_abertura"], "%H:%M").time()
        clinica.horario_fechamento = datetime.strptime(novos_dados["horario_fechamento"], "%H:%M").time()
        
        self.__view.mostrar_mensagem("Clínica alterada com sucesso!")

    def excluir(self) -> None:
        self.listar()
        self.__view.mostrar_mensagem("Para EXCLUIR, informe o ID e aperte Enter nos demais campos:")
        dados = self.__view.mostrar_dados()
        
        clinica = next((c for c in self.__clinicas if c.id == dados["id"]), None)
        if not clinica:
            raise ValueError("Clínica não encontrada.")
            
        self.__clinicas.remove(clinica)
        self.__view.mostrar_mensagem("Clínica excluída com sucesso!")

    def listar(self) -> None:
        if not self.__clinicas:
            raise ValueError("Nenhuma clínica cadastrada no sistema.")
            
        print("\n--- Lista de Clínicas Cadastradas ---")
        for c in self.__clinicas:
            dados_dit = {
                "id": c.id,
                "nome": c.nome,
                "cidade": c.cidade,
                "descricao": c.descricao,
                "horario_abertura": c.horario_abertura.strftime("%H:%M"),
                "horario_fechamento": c.horario_fechamento.strftime("%H:%M")
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

    # Este getter é essencial para o AtendimentoController conseguir ler a lista de clínicas!
    @property
    def clinicas(self) -> list:
        return self.__clinicas
