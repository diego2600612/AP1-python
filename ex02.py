# Definindo as frases e textos que serão exibidos na tela
titulo = "Cálculo no carrinho de compras"
descricao = "Um cliente comprou dois livros, cada um por: "
conectivo = " e recebeu um desconto de: "
pergunta = "Quanto ele gastou?"
resposta = "Ele gastou: "

# Definindo os valores numéricos da compra
preco_unitario = 35.00  # Preço de cada livro
quantidade = 2          # Quantidade de itens comprados
desconto = 10.00        # Valor em reais do desconto concedido

# Realizando os cálculos matemáticos
subtotal = preco_unitario * quantidade  # Multiplica o preço pela quantidade (35.00 * 2 = 70.00)
valor_final = subtotal - desconto        # Subtrai o desconto do subtotal (70.00 - 10.00 = 60.00)

# Imprime o texto formatado no console usando f-strings
# \n quebra a linha e :.2f formata os números para exibir 2 casas decimais
print(
    f"{titulo}\n"
    f"{descricao}R$ {preco_unitario:.2f}{conectivo}R$ {desconto:.2f}\n"
    f"{pergunta}\n"
    f"{resposta}R$ {valor_final:.2f}"
)
