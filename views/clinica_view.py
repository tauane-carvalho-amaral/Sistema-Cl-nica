class ClinicaView:
    def mostrar_menu(self) -> int:
        print("\n" + "="*30)
        print("   MENU DE CLÍNICAS")
        print("="*30)
        print("1 - Incluir Clínica")
        print("2 - Alterar Clínica")
        print("3 - Excluir Clínica")
        print("4 - Listar Clínicas")
        print("0 - Voltar")
        print("="*30)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def mostrar_dados(self) -> dict:
        print("\n--- Informe os Dados da Clínica ---")
        try:
            id_clinica = int(input("ID da Clínica: "))
            # Dica de usabilidade: se for só para excluir, o usuário aperta Enter no resto
            nome = input("Nome (ou Enter para pular): ")
            cidade = input("Cidade (ou Enter para pular): ")
            descricao = input("Descrição (ou Enter para pular): ")
            horario_abertura = input("Horário de abertura HH:MM (ou Enter para pular): ")
            horario_fechamento = input("Horário de fechamento HH:MM (ou Enter para pular): ")
            
            return {
                "id": id_clinica,
                "nome": nome,
                "cidade": cidade,
                "descricao": descricao,
                "horario_abertura": horario_abertura,
                "horario_fechamento": horario_fechamento
            }
        except ValueError:
            raise ValueError("O ID digitado deve ser um número inteiro.")

    def mostrar_lista(self, dados: dict) -> None:
        print("-" * 40)
        print(f"ID: {dados['id']} | Nome: {dados['nome']}")
        print(f"Cidade: {dados['cidade']} | Descrição: {dados['descricao']}")
        print(f"Horário de Funcionamento: {dados['horario_abertura']} às {dados['horario_fechamento']}")

    def mostrar_mensagem(self, mensagem: str) -> None:
        print(f"\n[SUCESSO] {mensagem}")

    def exibir_erro(self, mensagem: str) -> None:
        print(f"\n[ERRO DO SISTEMA] {mensagem}")
