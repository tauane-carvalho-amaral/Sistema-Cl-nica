from views.relatorio_view import RelatorioView

class RelatorioController:
    # Recebe os controllers necessários para aceder às listas de dados
    def __init__(self, ctrl_atendimento, ctrl_clinica, ctrl_procedimento):
        self.__view = RelatorioView()
        self.__ctrl_atendimento = ctrl_atendimento
        self.__ctrl_clinica = ctrl_clinica
        self.__ctrl_procedimento = ctrl_procedimento

    def abrir_menu(self) -> None:
        opcoes = {
            1: self.clinica_mais_atendimentos,
            2: self.atendimento_mais_caro,
            3: self.atendimento_mais_barato,
            4: self.procedimento_popular,
            5: self.procedimento_mais_caro,
            6: self.procedimento_mais_barato
        }
        while True:
            opcao = self.__view.mostrar_menu()
            if opcao == 0:
                break
            elif opcao in opcoes:
                self.tratar_excecoes(opcoes[opcao])
            else:
                self.__view.exibir_erro("Opção inválida.")

    def clinica_mais_atendimentos(self) -> None:
        atendimentos = self.__ctrl_atendimento.atendimentos
        if not atendimentos:
            raise ValueError("Não há atendimentos registados para gerar este relatório.")

        contagem = {}
        for a in atendimentos:
            nome_clinica = a.clinica.nome
            contagem[nome_clinica] = contagem.get(nome_clinica, 0) + 1

        clinica_top = max(contagem, key=contagem.get)
        self.__view.mostrar_clinica_mais_atendimentos(clinica_top, contagem[clinica_top])

    def atendimento_mais_caro(self) -> None:
        atendimentos = self.__ctrl_atendimento.atendimentos
        if not atendimentos:
            raise ValueError("Não há atendimentos registados.")

        mais_caro = max(atendimentos, key=lambda a: a.valor_total)
        dados = {
            "id": mais_caro.id,
            "data": mais_caro.data.strftime("%d/%m/%Y"),
            "paciente": mais_caro.paciente.nome,
            "valor": mais_caro.valor_total
        }
        self.__view.mostrar_atendimento_mais_caro(dados)

    def atendimento_mais_barato(self) -> None:
        atendimentos = self.__ctrl_atendimento.atendimentos
        if not atendimentos:
            raise ValueError("Não há atendimentos registados.")

        mais_barato = min(atendimentos, key=lambda a: a.valor_total)
        dados = {
            "id": mais_barato.id,
            "data": mais_barato.data.strftime("%d/%m/%Y"),
            "paciente": mais_barato.paciente.nome,
            "valor": mais_barato.valor_total
        }
        self.__view.mostrar_atendimento_mais_barato(dados)

    def procedimento_popular(self) -> None:
        atendimentos = self.__ctrl_atendimento.atendimentos
        if not atendimentos:
            raise ValueError("Não há atendimentos registados para verificar procedimentos.")

        contagem = {}
        for a in atendimentos:
            for p in a.procedimentos:
                contagem[p.descricao] = contagem.get(p.descricao, 0) + 1

        if not contagem:
            raise ValueError("Nenhum procedimento foi realizado nos atendimentos atuais.")

        proc_top = max(contagem, key=contagem.get)
        self.__view.mostrar_procedimento_popular(proc_top, contagem[proc_top])

    def procedimento_mais_caro(self) -> None:
        procedimentos = self.__ctrl_procedimento.procedimentos
        if not procedimentos:
            raise ValueError("Não há procedimentos cadastrados no sistema.")

        mais_caro = max(procedimentos, key=lambda p: p.custo)
        dados = {"id": mais_caro.id, "descricao": mais_caro.descricao, "custo": mais_caro.custo}
        self.__view.mostrar_procedimento_mais_caro(dados)

    def procedimento_mais_barato(self) -> None:
        procedimentos = self.__ctrl_procedimento.procedimentos
        if not procedimentos:
            raise ValueError("Não há procedimentos cadastrados no sistema.")

        mais_barato = min(procedimentos, key=lambda p: p.custo)
        dados = {"id": mais_barato.id, "descricao": mais_barato.descricao, "custo": mais_barato.custo}
        self.__view.mostrar_procedimento_mais_barato(dados)

    def tratar_excecoes(self, funcao_metodo) -> None:
        try:
            funcao_metodo()
        except ValueError as e:
            self.__view.exibir_erro(str(e))
        except Exception as e:
            self.__view.exibir_erro(f"Erro Inesperado: {str(e)}")
