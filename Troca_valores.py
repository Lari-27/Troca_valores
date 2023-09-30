try:
    # Solicita ao usuário que insira um valor para a variável A e converte para um número inteiro
    A = int(input("Informe um valor para a variável A:"))

    # Solicita ao usuário que insira um valor para a variável B e converte para um número inteiro
    B = int(input("Informe um valor para a variável B:"))

    # Compara os valores de A e B
    if A > B:
        # Se A for maior que B, troca os valores sem usar uma variável auxiliar
        A, B = B, A

    # Imprime os valores atualizados de A e B
    print("O valor da variável A agora é:", A)
    print("O valor da variável B agora é:", B)

except ValueError:
    print("Por favor, insira valores numéricos válidos para A e B.")
