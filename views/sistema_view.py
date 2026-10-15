class SistemaView:
    
    def mostrar_menu(self) -> int:
        print("\n" + "="*40)
        print("    SISTEMA DE GESTÃO DE CLÍNICAS")
        print("="*40)
        print("1 - Módulo de Clínicas")
        print("2 - Módulo de Pessoas (Pacientes/Profissionais)")
        print("3 - Módulo de Tipos de Atendimento")
        print("4 - Módulo de Atendimentos (Agendamentos)")
        print("5 - Módulo de Procedimentos")
        print("6 - Módulo de Pagamentos")
        print("7 - Módulo de Relatórios")
        print("0 - Sair do Sistema")
        print("="*40)
        
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def mostrar_mensagem(self, mensagem: str) -> None:
        print(f"\n[SISTEMA] {mensagem}")

    def exibir_erro(self, mensagem: str) -> None:
        print(f"\n[ERRO DO SISTEMA] {mensagem}")
