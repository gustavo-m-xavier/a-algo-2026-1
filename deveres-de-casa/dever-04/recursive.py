def recursive_f(n: int) -> int:
    """
    Calcula o valor da função F(n) de forma recursiva.

    Definição da recorrência:
        F(1) = 2
        F(n) = 2 * F(n-1) + n^2, para n > 1

    A função chama a si mesma até atingir o caso base (n == 1).

    Complexidade:
        Tempo: O(2^n) (exponencial, devido às chamadas recursivas)
        Espaço: O(n) (profundidade da pilha de recursão)

    Parâmetros:
        n (int): Número inteiro positivo.

    Retorno:
        int: Valor de F(n).

    Levanta:
        ValueError: Se n < 1.
    """
    if n < 1:
        raise ValueError("n deve ser maior ou igual a 1")

    if n == 1:
        return 2

    return 2 * recursive_f(n - 1) + n**2


def main():
    """
    Função principal que solicita um valor ao usuário
    e exibe o resultado de F(n).
    """
    try:
        n = int(input("Digite um valor inteiro positivo para n: "))
        resultado = recursive_f(n)
        print(f"F({n}) = {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()