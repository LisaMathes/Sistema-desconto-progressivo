# =====================================================================
# SISTEMA DE DESCONTO PROGRESSIVO
# Desenvolvido para aplicação de regras de desconto baseadas no total
# =====================================================================

def calcular_desconto():
    print("--- Bem-vindo ao Sistema de Desconto Progressivo ---")
    
    # Entrada de dados: Solicita o valor total da compra ao usuário
    try:
        valor_compra = float(input("Digite o valor total da compra (R$): "))
    except ValueError:
        print("Erro: Por favor, insira um valor numérico válido.")
        return

    # Validação inicial: Garante que o valor inserido não é negativo
    if valor_compra < 0:
        print("Erro: O valor da compra não pode ser negativo.")
        return

    # Estrutura de Decisão: Define o percentual de desconto com base nas regras
    if valor_compra < 200.00:
        percentual_desconto = 0.05  # 5% de desconto
    elif valor_compra < 300.00:
        percentual_desconto = 0.10  # 10% de desconto
    else:
        percentual_desconto = 0.15  # 15% de desconto

    # Processamento: Calcula os valores de desconto e o total final
    valor_desconto = valor_compra * percentual_desconto
    total_a_pagar = valor_compra - valor_desconto

    # Saída de dados: Exibe os resultados formatados para o usuário
    print("\n--- RESUMO DA COMPRA ---")
    print(f"Valor original:     R$ {valor_compra:.2f}")
    print(f"Desconto aplicado:  {percentual_desconto * 100:.0f}% (R$ {valor_desconto:.2f})")
    print(f"Total a pagar:      R$ {total_a_pagar:.2f}")
    print("------------------------")

# Executa o programa
if __name__ == "__main__":
    calcular_desconto()
