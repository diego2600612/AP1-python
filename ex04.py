def validar_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("Idade não pode ser negativa. Tente novamente.")
                continue
            return idade
        except ValueError:
            print("Entrada inválida! Digite um número inteiro para a idade.")


def validar_ingresso():
    while True:
        resposta = input("Você possui ingresso? (Digite 'sim' ou 'nao'): ").strip().lower()
        if resposta in ["sim", "s", "yes", "y"]:
            return True
        if resposta in ["nao", "não", "n", "no"]:
            return False
        print("Resposta inválida! Digite 'sim' ou 'nao'.")


def classificar_acesso(idade, tem_ingresso):
    if idade < 16:
        return {
            "status": "negado",
            "mensagem": "Acesso não permitido",
            "motivo": "Idade mínima para acesso é 16 anos."
        }
    if idade >= 16 and tem_ingresso:
        return {
            "status": "permitido",
            "mensagem": "Entrada liberada",
            "motivo": "Idade e ingresso verificados com sucesso."
        }
    return {
        "status": "pendente",
        "mensagem": "Compre um ingresso",
        "motivo": "É necessário adquirir um ingresso para entrar."
    }


def exibir_resultado(idade, tem_ingresso, resultado):
    print("\n" + "=" * 50)
    print("           RESULTADO DA CLASSIFICAÇÃO")
    print("=" * 50)
    print(f"Idade informada:        {idade} anos")
    print(f"Possui ingresso:        {'Sim' if tem_ingresso else 'Não'}")
    print("-" * 50)
    print(f"Status:                 {resultado['mensagem'].upper()}")
    print(f"Motivo: {resultado['motivo']}")
    print("=" * 50)


def main():
    idade = validar_idade()
    tem_ingresso = validar_ingresso()
    resultado = classificar_acesso(idade, tem_ingresso)
    exibir_resultado(idade, tem_ingresso, resultado)


main()