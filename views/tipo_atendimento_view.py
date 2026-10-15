class TipoAtendimentoView:
    def mostrar_menu(self) -> int:
        print("\n" + "="*35)
        print("   MENU DE TIPOS DE ATENDIMENTO")
        print("="*35)
        print("1 - Incluir Tipo de Atendimento")
        print("2 - Alterar Tipo de Atendimento")
        print("3 - Excluir Tipo de Atendimento")
        print("4 - Listar Tipos de Atendimento")
        print("0 - Voltar")
        print("="*35)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def mostrar_dados(self) -> dict:
        print("\n--- Dados do Tipo de Atendimento ---")
        try:
            id_tipo = int(input("ID do Tipo (ex: 1): "))
            nome = input("Nome (ex: Consulta, Exame - ou Enter para pular): ")
            descricao = input("Descrição (ou Enter para pular): ")
            
            return {
                "id": id_tipo,
                "nome": nome,
                "descricao": descricao
            }
        except ValueError:
            raise ValueError("O ID deve ser obrigatoriamente um número inteiro.")

    def mostrar_lista(self, dados: dict) -> None:
        print("-" * 40)
        print(f"ID: {dados['id']} | Nome: {dados['nome']}")
        print(f"Descrição: {dados['descricao']}")

    def mostrar_mensagem(self, mensagem: str) -> None:
        print(f"\n[SUCESSO] {mensagem}")

    def exibir_erro(self, mensagem: str) -> None:
        print(f"\n[ERRO DO SISTEMA] {mensagem}")
