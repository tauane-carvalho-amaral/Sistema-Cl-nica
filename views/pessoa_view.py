class PessoaView:
    def mostrar_menu(self) -> int:
        print("\n" + "="*35)
        print("   MENU DE PESSOAS (Cadastro)")
        print("="*35)
        print("1 - Incluir Pessoa (Paciente/Profissional)")
        print("2 - Alterar Pessoa")
        print("3 - Excluir Pessoa")
        print("4 - Listar Pessoas")
        print("0 - Voltar")
        print("="*35)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def mostrar_dados(self) -> dict:
        print("\n--- Inserir Dados ---")
        try:
            tipo = input("Selecione o Tipo (1 - Paciente | 2 - Profissional de Saúde): ")
            if tipo not in ['1', '2']:
                raise ValueError("Tipo inválido. Escolha 1 ou 2.")

            id_pessoa = int(input("ID: "))
            nome = input("Nome (ou Enter para pular na exclusão): ")
            cpf = input("CPF (ou Enter para pular): ")
            data_nasc = input("Data de Nascimento (DD/MM/AAAA) (ou Enter para pular): ")
            
            dados = {
                "tipo": tipo,
                "id": id_pessoa,
                "nome": nome,
                "cpf": cpf,
                "data_nascimento": data_nasc
            }
            
            # Pede atributos específicos apenas se for Profissional de Saúde
            if tipo == '2':
                dados["especialidade"] = input("Especialidade (ou Enter para pular): ")
                dados["registro_profissional"] = input("Registro Profissional (ou Enter para pular): ")
                
            return dados
        except ValueError as e:
            # Propaga o erro para o Controller apanhar
            raise ValueError(f"Dados incorretos: {e}")

    def mostrar_lista(self, dados: dict) -> None:
        print("-" * 40)
        print(f"ID: {dados['id']} | Categoria: {dados['tipo']}")
        print(f"Nome: {dados['nome']} | CPF: {dados['cpf']}")
        print(f"Data de Nascimento: {dados['data_nascimento']}")
        if dados['tipo'] == 'Profissional':
            print(f"Especialidade: {dados['especialidade']} | Registro: {dados['registro_profissional']}")

    def mostrar_mensagem(self, mensagem: str) -> None:
        print(f"\n[SUCESSO] {mensagem}")

    def exibir_erro(self, mensagem: str) -> None:
        print(f"\n[ERRO DO SISTEMA] {mensagem}")
