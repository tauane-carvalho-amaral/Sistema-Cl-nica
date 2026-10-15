class RelatorioView:
    def mostrar_menu(self) -> int:
        print("\n" + "="*40)
        print("         MENU DE RELATÓRIOS")
        print("="*40)
        print("1 - Clínica com Maior Número de Atendimentos")
        print("2 - Atendimento Mais Caro")
        print("3 - Atendimento Mais Barato")
        print("4 - Procedimento Mais Realizado (Popular)")
        print("5 - Procedimento Mais Caro")
        print("6 - Procedimento Mais Barato")
        print("0 - Voltar")
        print("="*40)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def mostrar_clinica_mais_atendimentos(self, clinica_nome: str, total: int) -> None:
        print("\n--- Clínica com Maior Número de Atendimentos ---")
        print(f"Clínica: {clinica_nome} | Total de Atendimentos: {total}")

    def mostrar_atendimento_mais_caro(self, dados: dict) -> None:
        print("\n--- Atendimento Mais Caro ---")
        print(f"ID: {dados['id']} | Data: {dados['data']} | Paciente: {dados['paciente']}")
        print(f"Valor Total: R$ {dados['valor']:.2f}")

    def mostrar_atendimento_mais_barato(self, dados: dict) -> None:
        print("\n--- Atendimento Mais Barato ---")
        print(f"ID: {dados['id']} | Data: {dados['data']} | Paciente: {dados['paciente']}")
        print(f"Valor Total: R$ {dados['valor']:.2f}")

    def mostrar_procedimento_popular(self, nome: str, qtd: int) -> None:
        print("\n--- Procedimento Mais Realizado ---")
        print(f"Procedimento: {nome} | Quantidade de Realizações: {qtd}")

    def mostrar_procedimento_mais_caro(self, dados: dict) -> None:
        print("\n--- Procedimento Mais Caro ---")
        print(f"ID: {dados['id']} | Descrição: {dados['descricao']} | Custo: R$ {dados['custo']:.2f}")

    def mostrar_procedimento_mais_barato(self, dados: dict) -> None:
        print("\n--- Procedimento Mais Barato ---")
        print(f"ID: {dados['id']} | Descrição: {dados['descricao']} | Custo: R$ {dados['custo']:.2f}")

    def mostrar_mensagem(self, msg: str) -> None:
        print(f"\n[INFO] {msg}")

    def exibir_erro(self, mensagem: str) -> None:
        print(f"\n[ERRO DO SISTEMA] {mensagem}")
