# Resultados de Execução

```
Teste de desempenho do fatorial recursivo

n = 10
Tempo de execução: 0.0000044000 segundos
----------------------------------------
n = 100
Tempo de execução: 0.0000182000 segundos
----------------------------------------
n = 500
Tempo de execução: 0.0001552000 segundos
----------------------------------------
n = 1000
Tempo de execução: 0.0004043000 segundos
----------------------------------------
```

# Explicação do Funcionamento do Algoritmo

O **fatorial de um número n** é definido como: n! = n _ (n-1) _ (n-2) _ ... _ 1

Na versão **recursiva**, usamos a definição matemática: n! = n \* (n-1)!

Com o **caso base**: 0! = 1

Exemplo para **n = 4**:

```
fatorial(4)
= 4 * fatorial(3)
= 4 * (3 * fatorial(2))
= 4 * (3 * (2 * fatorial(1)))
= 4 * (3 * (2 * 1))
= 24
```

A pilha de chamadas fica:

```
fatorial(4)
fatorial(3)
fatorial(2)
fatorial(1)
```

# Análise da Complexidade Assintótica

## Número de operações

A função chama a si mesma **uma vez para cada valor até chegar a 1**.

Número de chamadas:

```
fatorial(n)
fatorial(n-1)
fatorial(n-2)
...
fatorial(1)
```

Total:

Cada chamada faz apenas:

- uma comparação
- uma multiplicação
- uma chamada recursiva

Ou seja, **tempo constante por chamada**.

## Complexidade de Tempo

Portanto, o tempo total é proporcional a **n**.

T(n) = T(n-1) + O(1)

Resolvendo a recorrência: T(n) = O(n)

**Complexidade de tempo:** O(n)

## Complexidade de Espaço

Como o algoritmo usa **recursão**, cada chamada fica na **pilha de execução (call stack)**.

Profundidade da recursão:

```
n chamadas
```

Logo: O(n)

**Complexidade de espaço:** O(n)
