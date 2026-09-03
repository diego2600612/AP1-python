import locale


def configurar_formatacao_monetaria():
    for local in ("pt_BR.UTF-8", "Portuguese_Brazil.1252"):
        try:
            locale.setlocale(locale.LC_ALL, local)
            return True
        except locale.Error:
            pass
    return False


def formatar_real(valor):
    if configurar_formatacao_monetaria():
        return locale.currency(valor, grouping=True, symbol="R$ ")
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def calcular_compra(preco, quantidade, percentual_desconto):
    subtotal = preco * quantidade
    valor_desconto = subtotal * (percentual_desconto / 100)
    total_final = subtotal - valor_desconto
    valor_medio = total_final / quantidade if quantidade else 0

    return {
        "subtotal": subtotal,
        "valor_desconto": valor_desconto,
        "total_final": total_final,
        "valor_medio": valor_medio,
    }


def mostrar_cabecalho():
    print("=" * 50)
    print("         SISTEMA DE COMPRAS")
    print("=" * 50)


def mostrar_recibo(nome_cliente, produto, preco, quantidade, percentual_desconto, dados_compra):
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
    mostrar_cabecalho()

    nome_cliente = input("Nome do cliente: ")
    produto = input("Nome do produto: ")
    preco = float(input("Preco unitario (R$): "))
    quantidade = int(input("Quantidade: "))
    percentual_desconto = float(input("Percentual de desconto (%): "))

    dados_compra = calcular_compra(preco, quantidade, percentual_desconto)

    mostrar_recibo(nome_cliente, produto, preco, quantidade, percentual_desconto, dados_compra)

    print("Processando dados", end="... ")
    print("Finalizado!", end="\n\n")


main()