# Análise de Complexidade de Algoritmos

Este projeto apresenta a implementação e análise de complexidade de três problemas clássicos da computação:

- Algoritmo de ordenação Merge Sort
- Multiplicação de Matrizes
- Resolução de Recorrências utilizando o Teorema Mestre

O objetivo é compreender como o tempo de execução cresce em função do tamanho da entrada.

---

## 1. Merge Sort

O Merge Sort é um algoritmo de ordenação baseado na estratégia de **divisão e conquista**. Ele divide o vetor em partes menores, ordena cada uma recursivamente e depois realiza a junção (merge).

### Recorrência

T(n) = 2T(n/2) + n

- 2T(n/2): o problema é dividido em duas partes iguais
- n: custo para intercalar (merge) os elementos

### Análise

Aplicando o Teorema Mestre:

- a = 2
- b = 2
- f(n) = n

Temos:

n^(log_b a) = n^(log₂ 2) = n

Como f(n) = n, estamos no **Caso 2 do Teorema Mestre**.

### Complexidade Final

O(n log n)

Isso ocorre porque existem log(n) níveis de recursão, e em cada nível o custo é linear.

---

## 2. Multiplicação de Matrizes

A multiplicação de matrizes foi implementada utilizando três laços de repetição aninhados.

### Funcionamento

Para cada elemento da matriz resultado, é necessário calcular a soma dos produtos entre linhas e colunas.

### Complexidade

Considerando:

- Matriz A de dimensão n × p
- Matriz B de dimensão p × m

A complexidade é:

O(n × m × p)

### Caso Especial (matrizes quadradas)

Quando n = m = p:

O(n³)

Isso ocorre devido aos três loops aninhados.

---

## 3. Resolução de Recorrências

Foram analisadas três recorrências utilizando o **Teorema Mestre**, que permite determinar a complexidade de funções recursivas da forma:

T(n) = aT(n/b) + f(n)

---

### 3.1 Recorrência 1

T(n) = 2T(n/4) + √n

#### Análise:

- a = 2
- b = 4
- f(n) = n^(1/2)

Calculando:

log₄(2) = 1/2

Logo:

n^(log_b a) = n^(1/2)

Como f(n) = n^(1/2), temos o **Caso 2** do Teorema Mestre.

#### Resultado:

Θ(√n log n)

---

### 3.2 Recorrência 2

T(n) = 2T(n/4) + n

#### Análise:

- a = 2
- b = 4
- f(n) = n

n^(log_b a) = n^(1/2)

Como f(n) cresce mais rápido que n^(1/2), temos o **Caso 3** do Teorema Mestre.

#### Resultado:

Θ(n)

---

### 3.3 Recorrência 3

T(n) = 16T(n/4) + n²

#### Análise:

- a = 16
- b = 4
- f(n) = n²

log₄(16) = 2

Logo:

n^(log_b a) = n²

Como f(n) = n², temos o **Caso 2** do Teorema Mestre.

#### Resultado:

Θ(n² log n)

---

## Conclusão

A análise de complexidade permite entender o comportamento dos algoritmos em grandes entradas:

- Merge Sort apresenta alta eficiência: **O(n log n)**
- Multiplicação de matrizes tradicional possui custo cúbico: **O(n³)**
- Recorrências podem variar bastante, indo de crescimento linear até exponencial ou logarítmico

Esses resultados reforçam a importância de escolher algoritmos eficientes para garantir bom desempenho em aplicações reais.
