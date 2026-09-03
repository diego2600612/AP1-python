titulo = "Cálculo no carrinho de compras"
descricao = "Um cliente comprou dois livros, cada um por: "
conectivo = " e recebeu um desconto de: "
pergunta = "Quanto ele gastou?"
resposta = "Ele gastou: "

preco_unitario = 35.00
quantidade = 2
desconto = 10.00

subtotal = preco_unitario * quantidade
valor_final = subtotal - desconto

print(
    f"{titulo}\n"
    f"{descricao}R$ {preco_unitario:.2f}{conectivo}R$ {desconto:.2f}\n"
    f"{pergunta}\n"
    f"{resposta}R$ {valor_final:.2f}"
)