import locale  # Módulo para adaptar o programa às convenções regionais (moeda, datas, etc.)


def configurar_formatacao_monetaria():
    """Tenta configurar a localização para o padrão brasileiro (Windows e Linux/Mac).
    Retorna True se conseguir e False se o sistema não suportar o locale pt_BR.
    """
    for local in ("pt_BR.UTF-8", "Portuguese_Brazil.1252"):
        try:
            locale.setlocale(locale.LC_ALL, local)
            return True
        except locale.Error:
            pass
    return False


def formatar_real(valor):
    """Converte um número float para o formato de moeda brasileira (R$ 0,00).
    Usa a biblioteca 'locale' se disponível; caso contrário, formata manualmente via f-string.
    """
    if configurar_formatacao_monetaria():
        return locale.currency(valor, grouping=True, symbol="R$ ")
    # Fallback manual: troca vírgulas por pontos para seguir o padrão brasileiro
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def calcular_compra(preco, quantidade, percentual_desconto):
    """Realiza os cálculos financeiros da compra.
    Retorna um dicionário com subtotal, valor do desconto, total a pagar e valor médio por item.
    """
    subtotal = preco * quantidade
    valor_desconto = subtotal * (percentual_desconto / 100)
    total_final = subtotal - valor_desconto
    # Evita divisão por zero caso a quantidade seja 0
    valor_medio = total_final / quantidade if quantidade else 0

    return {
        "subtotal": subtotal,
        "valor_desconto": valor_desconto,
        "total_final": total_final,
        "valor_medio": valor_medio,
    }


def mostrar_cabecalho():
    """Exibe o cabeçalho inicial do sistema formatado com linhas de sinal de igual."""
    print("=" * 50)
    print("         SISTEMA DE COMPRAS")
    print("=" * 50)


def mostrar_recibo(nome_cliente, produto, preco, quantidade, percentual_desconto, dados_compra):
    """Imprime na tela um recibo detalhado com os dados do cliente, produto e valores calculados."""
    print("\n" + "=" * 50)
    print("         RECIBO DA COMPRA")
    print("=" * 50)

    print(f"Cliente:          {nome_cliente}")
    print(f"Produto:          {produto}")
    print(f"Quantidade:       {quantidade} unidade(s)")
    print(f"Preco unitario:   R$ {formatar_real(preco)}")
    print("-" * 50)
    print(f"Subtotal:         R$ {formatar_real(dados_compra['subtotal'])}")
    print(f"Desconto:         {percentual_desconto:.0f}% (R$ {formatar_real(dados_compra['valor_desconto'])})")
    print("-" * 50)
    print(f"TOTAL A PAGAR:    R$ {formatar_real(dados_compra['total_final'])}")
    print(f"\nValor medio por unidade: R$ {formatar_real(dados_compra['valor_medio'])}")

    print("\n" + "=" * 50)
    print("          OBRIGADO PELA COMPRA!")
    print("=" * 50)


def main():
    """Função principal que orquestra o fluxo do programa:
    1. Mostra o cabeçalho
    2. Coleta os dados digitados pelo usuário
    3. Chama a função de cálculo
    4. Exibe o recibo final
    """
    mostrar_cabecalho()

    # Entrada de dados do usuário
    nome_cliente = input("Nome do cliente: ")
    produto = input("Nome do produto: ")
    preco = float(input("Preco unitario (R$): "))
    quantidade = int(input("Quantidade: "))
    percentual_desconto = float(input("Percentual de desconto (%): "))

    # Processamento dos cálculos
    dados_compra = calcular_compra(preco, quantidade, percentual_desconto)

    # Saída do recibo
    mostrar_recibo(nome_cliente, produto, preco, quantidade, percentual_desconto, dados_compra)

    # Mensagem final de encerramento
    print("Processando dados", end="... ")
    print("Finalizado!", end="\n\n")


# Executa a função principal do script
main()
