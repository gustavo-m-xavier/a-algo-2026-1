def palindrome(arr, n):
    for i in range(n //2):
        if arr[i] != arr[n - i - 1]:
            print("Não é um palíndromo")
            return
    print("É um palíndromo")

def main():
    n = int(input("Digite o tamanho do array: "))
    arr = []
    for i in range(n):
        num = input(f"Digite o elemento {i + 1}: ")
        arr.append(num)
    palindrome(arr, n)

if __name__ == "__main__":
    main()