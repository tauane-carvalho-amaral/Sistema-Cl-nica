class ProcedimentoView:
    def mostrar_menu(self) -> int:
        print("\n" + "="*30)
        print("   MENU DE PROCEDIMENTOS")
        print("="*30)
        print("1 - Incluir Procedimento")
        print("2 - Alterar Procedimento")
        print("3 - Excluir Procedimento")
        print("4 - Listar Procedimentos")
        print("0 - Voltar")
        print("="*30)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def mostrar_dados(self) -> dict:
        print("\n--- Dados do Procedimento ---")
        try:
            id_proc = int(input("ID do Procedimento: "))
            descricao = input("Descrição (ex: Limpeza, Curativo - ou Enter para pular): ")
            
            custo_str = input("Custo em R$ (ex: 150.50 - ou Enter para pular): ")
            custo = float(custo_str) if custo_str else 0.0
            
            id_prof = input("ID do Profissional Responsável (ou Enter para pular): ")
            id_profissional = int(id_prof) if id_prof else None
            
            return {
                "id": id_proc,
                "descricao": descricao,
                "custo": custo,
                "id_profissional": id_profissional
            }
        except ValueError:
            raise ValueError("ID e ID do Profissional devem ser inteiros. Custo deve ser numérico.")

    def mostrar_lista(self, dados: dict) -> None:
        print("-" * 40)
        print(f"ID: {dados['id']} | Descrição: {dados['descricao']}")
        print(f"Custo: R$ {dados['custo']:.2f}")
        print(f"Profissional Responsável: {dados['profissional']}")

    def mostrar_mensagem(self, mensagem: str) -> None:
        print(f"\n[SUCESSO] {mensagem}")

    def exibir_erro(self, mensagem: str) -> None:
        print(f"\n[ERRO] {mensagem}")
