def validar_idade():
    """Solicita a idade do usuário repetidamente até que seja digitado
    um número inteiro válido e não negativo.
    """
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("Idade não pode ser negativa. Tente novamente.")
                continue
            return idade
        except ValueError:
            # Trata o erro caso o usuário digite texto em vez de números
            print("Entrada inválida! Digite um número inteiro para a idade.")


def validar_ingresso():
    """Pergunta se o usuário tem ingresso e aceita variações de respostas válidas (sim/s/yes/y ou nao/não/n/no).
    Retorna True se tiver ingresso e False se não tiver.
    """
    while True:
        # .strip() remove espaços extras e .lower() padroniza para letras minúsculas
        resposta = input("Você possui ingresso? (Digite 'sim' ou 'nao'): ").strip().lower()
        if resposta in ["sim", "s", "yes", "y"]:
            return True
        if resposta in ["nao", "não", "n", "no"]:
            return False
        print("Resposta inválida! Digite 'sim' ou 'nao'.")


def classificar_acesso(idade, tem_ingresso):
    """Aplica as regras de negócio para liberar ou negar o acesso:
    - Menor de 16 anos: Acesso negado.
    - A partir de 16 anos com ingresso: Entrada liberada.
    - A partir de 16 anos sem ingresso: Status pendente (necessita comprar ingresso).
    Retorna um dicionário com o status, mensagem e motivo.
    """
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
    """Exibe um painel visualmente formatado no terminal com as informações
    coletadas e a decisão final sobre o acesso.
    """
    print("\n" + "=" * 50)
    print("           RESULTADO DA CLASSIFICAÇÃO")
    print("=" * 50)
    print(f"Idade informada:        {idade} anos")
    print(f"Possui ingresso:        {'Sim' if tem_ingresso else 'Não'}")
    print("-" * 50)
    # .upper() transforma a mensagem do status em letras maiúsculas
    print(f"Status:                 {resultado['mensagem'].upper()}")
    print(f"Motivo: {resultado['motivo']}")
    print("=" * 50)


def main():
    """Função principal que orquestra a execução do fluxo:
    1. Obtém e valida a idade
    2. Obtém e valida a posse do ingresso
    3. Processa a regra de acesso
    4. Exibe o resultado final
    """
    idade = validar_idade()
    tem_ingresso = validar_ingresso()
    resultado = classificar_acesso(idade, tem_ingresso)
    exibir_resultado(idade, tem_ingresso, resultado)


# Executa o programa chamando a função principal
main()
