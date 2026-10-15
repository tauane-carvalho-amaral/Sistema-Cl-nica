class PagamentoView:
    def mostrar_menu(self) -> int:
        print("\n" + "="*35)
        print("   MENU DE PAGAMENTOS")
        print("="*35)
        print("1 - Incluir Pagamento")
        print("2 - Alterar Pagamento")
        print("3 - Excluir Pagamento")
        print("4 - Listar Pagamentos")
        print("0 - Voltar")
        print("="*35)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def mostrar_dados(self) -> dict:
        print("\n--- Dados do Pagamento ---")
        try:
            id_pagamento = int(input("ID do Pagamento: "))
            
            # Para exclusão, o utilizador pode querer saltar os restantes campos
            id_atend_str = input("ID do Atendimento vinculado (ou Enter para pular): ")
            id_atendimento = int(id_atend_str) if id_atend_str else None
            
            data_pagamento = input("Data do Pagamento (DD/MM/AAAA) (ou Enter para pular): ")
            
            valor_str = input("Valor a pagar em R$ (ou Enter para pular): ")
            valor = float(valor_str) if valor_str else 0.0
            
            tipo = input("Modalidade (1-Dinheiro | 2-Pix | 3-Cartão) (ou Enter para pular): ")
            
            dados = {
                "id": id_pagamento,
                "id_atendimento": id_atendimento,
                "data": data_pagamento,
                "valor": valor,
                "tipo": tipo
            }
            
            # Dados específicos das classes filhas
            if tipo == '2':
                dados["cpf_pagador"] = input("CPF do Pagador (Pix): ")
            elif tipo == '3':
                dados["numero_cartao"] = input("Número do Cartão: ")
                dados["bandeira"] = input("Bandeira do Cartão: ")
                
            return dados
        except ValueError:
            raise ValueError("IDs devem ser inteiros e o valor deve ser numérico.")

    def mostrar_lista(self, dados: dict) -> None:
        print("-" * 40)
        print(f"ID Pagamento: {dados['id']} | Data: {dados['data']}")
        print(f"Atendimento Vinculado (ID): {dados['id_atendimento']}")
        print(f"Valor Pago: R$ {dados['valor']:.2f}")
        print(f"Valor Restante: R$ {dados['valor_restante']:.2f}")
        print(f"Modalidade: {dados['modalidade']}")
        if dados.get("detalhes"):
            print(f"Detalhes: {dados['detalhes']}")

    def mostrar_mensagem(self, mensagem: str) -> None:
        print(f"\n[SUCESSO] {mensagem}")

    def exibir_erro(self, mensagem: str) -> None:
        print(f"\n[ERRO DO SISTEMA] {mensagem}")
