class AtendimentoView:
    def mostrar_menu(self) -> int:
        print("\n" + "="*30)
        print("   MENU DE ATENDIMENTOS")
        print("="*30)
        print("1 - Incluir Atendimento")
        print("2 - Alterar Atendimento")
        print("3 - Excluir Atendimento")
        print("4 - Listar Atendimentos")
        print("0 - Voltar")
        print("="*30)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
        
    def mostrar_dados(self) -> dict:
        print("\n--- Inserir Dados do Atendimento ---")
        try:
            id_atendimento = int(input("ID do Atendimento: "))
            id_clinica = int(input("ID da Clínica vinculada: "))
            id_paciente = int(input("ID do Paciente: "))
            id_profissional = int(input("ID do Profissional de Saúde: "))
            id_tipo = int(input("ID do Tipo de Atendimento: "))
            
            data_str = input("Data (DD/MM/AAAA): ")
            horario_inicio = input("Horário de Início (HH:MM): ")
            horario_fim = input("Horário de Fim (HH:MM): ")
            
            # --- NOVA PERGUNTA DENTRO DO MESMO MÉTODO ---
            procedimentos_str = input("IDs dos Procedimentos (separados por vírgula, ou Enter para nenhum): ")
            
            return {
                "id": id_atendimento,
                "id_clinica": id_clinica,
                "id_paciente": id_paciente,
                "id_profissional": id_profissional,
                "id_tipo": id_tipo,
                "data": data_str,
                "horario_inicio": horario_inicio,
                "horario_fim": horario_fim,
                "procedimentos_str": procedimentos_str # <-- Retorna no dicionário
            }
        except ValueError:
            raise ValueError("Você digitou um texto onde deveria ser um número inteiro.")
    
    def selecionar_atendimento(self) -> int:
        # Método auxiliar padrão para permitir a alteração e exclusão exigidas no CRUD
        try:
            return int(input("\nDigite o ID do Atendimento que deseja selecionar: "))
        except ValueError:
            raise ValueError("O ID deve ser um número inteiro.")

    def mostrar_lista(self, dados: dict) -> None:
        print("-" * 40)
        print(f"Atendimento ID: {dados['id']} | Data: {dados['data']}")
        print(f"Clínica: {dados['clinica']} | Tipo: {dados['tipo']}")
        print(f"Paciente: {dados['paciente']} | Profissional: {dados['profissional']}")
        print(f"Horário: {dados['horario_inicio']} às {dados['horario_fim']}")
        print(f"Valor Total: R$ {dados['valor_total']:.2f}")

    def mostrar_mensagem(self, mensagem: str) -> None:
        print(f"\n[SUCESSO] {mensagem}")

    def exibir_erro(self, mensagem: str) -> None:
        print(f"\n[ERRO DO SISTEMA] {mensagem}")
