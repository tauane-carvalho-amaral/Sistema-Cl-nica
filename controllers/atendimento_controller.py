from views.atendimento_view import AtendimentoView
from models.model_atendimento import Atendimento
from datetime import datetime

class AtendimentoController:
    def __init__(self, clinicas: list, pacientes: list, profissionais: list, tipos: list, procedimentos: list):
        self.__view = AtendimentoView()
        self.__atendimentos = []
        self.__clinicas = clinicas
        self.__pacientes = pacientes
        self.__profissionais = profissionais
        self.__tipos = tipos
        self.__procedimentos_cadastrados = procedimentos

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
                # Chama a função de tratamento de exceções passando o método escolhido
                self.tratar_excecoes(opcoes[opcao])
            else:
                self.__view.exibir_erro("Opção inválida selecionada.")

    def incluir(self) -> None:
        dados = self.__view.mostrar_dados()
        
        if any(a.id == dados["id"] for a in self.__atendimentos):
            raise ValueError("Já existe um atendimento registrado com este ID.")

        clinica_obj = next((c for c in self.__clinicas if c.id == dados["id_clinica"]), None)
        paciente_obj = next((p for p in self.__pacientes if p.id == dados["id_paciente"]), None)
        prof_obj = next((p for p in self.__profissionais if p.id == dados["id_profissional"]), None)
        tipo_obj = next((t for t in self.__tipos if t.id == dados["id_tipo"]), None)

        if not all([clinica_obj, paciente_obj, prof_obj, tipo_obj]):
            raise ValueError("Um ou mais IDs informados (Clínica, Paciente, Profissional ou Tipo) não existem no sistema.")

        data_obj = datetime.strptime(dados["data"], "%d/%m/%Y").date()
        inicio_obj = datetime.strptime(dados["horario_inicio"], "%H:%M").time()
        fim_obj = datetime.strptime(dados["horario_fim"], "%H:%M").time()

        procedimentos_do_atendimento = []
        valor_total = 0.0
        
        if dados.get("procedimentos_str") and dados["procedimentos_str"].strip():
            lista_ids_str = dados["procedimentos_str"].split(",")
            for id_str in lista_ids_str:
                try:
                    p_id = int(id_str.strip())
                    proc = next((p for p in self.__procedimentos_cadastrados if p.id == p_id), None)
                    if proc:
                        procedimentos_do_atendimento.append(proc)
                        valor_total += proc.custo
                    else:
                        self.__view.exibir_erro(f"Procedimento ID {p_id} ignorado (não encontrado no sistema).")
                except ValueError:
                    self.__view.exibir_erro(f"O valor '{id_str}' não é um ID válido e foi ignorado.")

        novo_atendimento = Atendimento(
            id=dados["id"],
            clinica=clinica_obj,
            paciente=paciente_obj,
            profissional=prof_obj,
            data=data_obj,
            horario_inicio=inicio_obj,
            horario_fim=fim_obj,
            tipo_atendimento=tipo_obj,
            procedimentos=procedimentos_do_atendimento, 
            valor_total=valor_total                     
        )

        novo_atendimento.validar_regras_agendamento()
        
        self.__atendimentos.append(novo_atendimento)
        self.__view.mostrar_mensagem("Atendimento agendado e validado com sucesso!")
    
    def alterar(self) -> None:
        self.listar()
        id_selecionado = self.__view.selecionar_atendimento()
        
        atendimento = next((a for a in self.__atendimentos if a.id == id_selecionado), None)
        if not atendimento:
            raise ValueError("Atendimento não encontrado no sistema.")

        self.__view.mostrar_mensagem("Insira os novos dados para este atendimento:")
        novos_dados = self.__view.mostrar_dados()
        
        clinica_obj = next((c for c in self.__clinicas if c.id == novos_dados["id_clinica"]), None)
        paciente_obj = next((p for p in self.__pacientes if p.id == novos_dados["id_paciente"]), None)
        prof_obj = next((p for p in self.__profissionais if p.id == novos_dados["id_profissional"]), None)
        tipo_obj = next((t for t in self.__tipos if t.id == novos_dados["id_tipo"]), None)

        if not all([clinica_obj, paciente_obj, prof_obj, tipo_obj]):
            raise ValueError("Erro: Os novos IDs vinculados não foram encontrados.")

        atendimento.clinica = clinica_obj
        atendimento.paciente = paciente_obj
        atendimento.profissional = prof_obj
        atendimento.tipo_atendimento = tipo_obj
        atendimento.data = datetime.strptime(novos_dados["data"], "%d/%m/%Y").date()
        atendimento.horario_inicio = datetime.strptime(novos_dados["horario_inicio"], "%H:%M").time()
        atendimento.horario_fim = datetime.strptime(novos_dados["horario_fim"], "%H:%M").time()
        
        atendimento.validar_regras_agendamento()
        self.__view.mostrar_mensagem("Atendimento alterado com sucesso!")

    def excluir(self) -> None:
        self.listar()
        id_selecionado = self.__view.selecionar_atendimento()
        
        for atendimento in self.__atendimentos:
            if atendimento.id == id_selecionado:
                self.__atendimentos.remove(atendimento)
                self.__view.mostrar_mensagem("Atendimento excluído com sucesso!")
                return
                
        raise ValueError("ID de Atendimento não encontrado.")

    def listar(self) -> None:
        if not self.__atendimentos:
            raise ValueError("Não há atendimentos registrados para listar.")
            
        for a in self.__atendimentos:
            dados = {
                "id": a.id,
                "data": a.data.strftime("%d/%m/%Y"),
                "clinica": a.clinica.nome,
                "tipo": a.tipo_atendimento.nome,
                "paciente": a.paciente.nome,
                "profissional": a.profissional.nome,
                "horario_inicio": a.horario_inicio.strftime("%H:%M"),
                "horario_fim": a.horario_fim.strftime("%H:%M"),
                "valor_total": a.valor_total
            }
            self.__view.mostrar_lista(dados)

    def tratar_excecoes(self, metodo_alvo) -> None:
        try:
            metodo_alvo()
        except ValueError as e:
            self.__view.exibir_erro(f"Erro de Validação/Dados: {e}")
        except TypeError as e:
            self.__view.exibir_erro(f"Erro de Tipagem: {e}")
        except Exception as e:
            self.__view.exibir_erro(f"Falha Crítica Inesperada: {e}")

    @property
    def atendimentos(self) -> list:
        return self.__atendimentos
