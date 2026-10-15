from views.pessoa_view import PessoaView
from models.model_pessoa_paciente import Paciente
from models.model_pessoa_profissional_saude import ProfissionalSaude
from datetime import datetime

class PessoaController:
    def __init__(self):
        self.__view = PessoaView()
        # Separamos em duas listas para facilitar o envio ao AtendimentoController depois
        self.__pacientes = []
        self.__profissionais = []

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
        
        # Valida se o ID já existe juntando as duas listas momentaneamente
        if any(p.id == dados["id"] for p in self.__pacientes + self.__profissionais):
            raise ValueError("Já existe um registo com este ID.")
            
        if not dados["nome"] or not dados["cpf"] or not dados["data_nascimento"]:
            raise ValueError("Nome, CPF e Data de Nascimento são campos obrigatórios.")
            
        data_nasc_obj = datetime.strptime(dados["data_nascimento"], "%d/%m/%Y").date()
        
        # 1 - Instancia Paciente
        if dados["tipo"] == '1':
            novo_paciente = Paciente(
                id=dados["id"], 
                nome=dados["nome"], 
                cpf=dados["cpf"], 
                data_nascimento=data_nasc_obj
            )
            self.__pacientes.append(novo_paciente)
            self.__view.mostrar_mensagem("Paciente registado com sucesso!")
            
        # 2 - Instancia Profissional de Saúde
        elif dados["tipo"] == '2':
            if not dados.get("especialidade") or not dados.get("registro_profissional"):
                raise ValueError("Especialidade e Registo Profissional são obrigatórios para médicos.")
                
            novo_profissional = ProfissionalSaude(
                id=dados["id"], 
                nome=dados["nome"], 
                cpf=dados["cpf"], 
                data_nascimento=data_nasc_obj,
                especialidade=dados["especialidade"],
                registro_profissional=dados["registro_profissional"]
            )
            self.__profissionais.append(novo_profissional)
            self.__view.mostrar_mensagem("Profissional de Saúde registado com sucesso!")

    def alterar(self) -> None:
        self.listar()
        self.__view.mostrar_mensagem("Para ALTERAR, insira o Tipo (1 ou 2), o ID atual e os novos dados:")
        novos_dados = self.__view.mostrar_dados()
        
        # Define em qual lista procurar
        lista_alvo = self.__pacientes if novos_dados["tipo"] == '1' else self.__profissionais
        pessoa = next((p for p in lista_alvo if p.id == novos_dados["id"]), None)
        
        if not pessoa:
            raise ValueError("Registo não encontrado no sistema.")
            
        pessoa.nome = novos_dados["nome"]
        pessoa.cpf = novos_dados["cpf"]
        pessoa.data_nascimento = datetime.strptime(novos_dados["data_nascimento"], "%d/%m/%Y").date()
        
        if novos_dados["tipo"] == '2':
            pessoa.especialidade = novos_dados["especialidade"]
            pessoa.registro_profissional = novos_dados["registro_profissional"]
            
        self.__view.mostrar_mensagem("Cadastro alterado com sucesso!")

    def excluir(self) -> None:
        self.listar()
        self.__view.mostrar_mensagem("Para EXCLUIR, insira o Tipo e o ID (carregue em Enter nos restantes):")
        dados = self.__view.mostrar_dados()
        
        lista_alvo = self.__pacientes if dados["tipo"] == '1' else self.__profissionais
        pessoa = next((p for p in lista_alvo if p.id == dados["id"]), None)
        
        if not pessoa:
            raise ValueError("Registo não encontrado.")
            
        lista_alvo.remove(pessoa)
        self.__view.mostrar_mensagem("Cadastro eliminado com sucesso!")

    def listar(self) -> None:
        if not self.__pacientes and not self.__profissionais:
            raise ValueError("Não há pessoas registadas no sistema.")
            
        print("\n--- PACIENTES ---")
        for p in self.__pacientes:
            dados_dit = {
                "tipo": "Paciente",
                "id": p.id,
                "nome": p.nome,
                "cpf": p.cpf,
                "data_nascimento": p.data_nascimento.strftime("%d/%m/%Y")
            }
            self.__view.mostrar_lista(dados_dit)
            
        print("\n--- PROFISSIONAIS DE SAÚDE ---")
        for p in self.__profissionais:
            dados_dit = {
                "tipo": "Profissional",
                "id": p.id,
                "nome": p.nome,
                "cpf": p.cpf,
                "data_nascimento": p.data_nascimento.strftime("%d/%m/%Y"),
                "especialidade": p.especialidade,
                "registro_profissional": p.registro_profissional
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
            self.__view.exibir_erro(f"Ocorreu um erro crítico: {e}")

    # Properties (Getters) necessários para interligar as classes no SistemaController
    @property
    def pacientes(self) -> list:
        return self.__pacientes
        
    @property
    def profissionais(self) -> list:
        return self.__profissionais