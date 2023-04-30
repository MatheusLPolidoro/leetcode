# Inteiros para algarismos romanos

Os algarismos romanos são representados por sete símbolos diferentes: I, V, X, L, C, D e M.

Valor | símbolo
|--|--|
|I | 1|
|V | 5|
|X | 10|
|L | 50|
|C | 100|
|D | 500|
|M | 1000|

Por exemplo, 2 é escrito como II em algarismo romano, apenas dois um são somados. 12 é escrito como XII, que é simplesmente X + II. O número 27 é escrito como XXVII, que é XX + V + II.

Os algarismos romanos geralmente são escritos do maior para o menor, da esquerda para a direita. No entanto, o numeral para quatro não é IIII. Em vez disso, o número quatro é escrito como IV. Como o um vem antes do cinco, nós o subtraímos, resultando em quatro. O mesmo princípio se aplica ao número nove, que é escrito como IX. Existem seis instâncias em que a subtração é usada:

**I** pode ser colocado antes de **V (5)** e **X (10)** para formar 4 e 9.  
**X** pode ser colocado antes de **L (50)** e **C (100)** para fazer 40 e 90.  
**C** pode ser colocado antes de **D (500)** e **M (1000)** para fazer 400 e 900.  
Dado um número inteiro, converta-o em um numeral romano.  

## Exemplos:
```
Entrada: num = 3
Saída: "III"
Explicação: 3 é representado como 3 uns.
```
```
Entrada: num = 58
Saída: "LVIII"
Explicação: L = 50, V = 5, III = 3.
```
```
Entrada: num = 1994
Saída: "MCMXCIV"
Explicação: M = 1000, CM = 900, XC = 90 e IV = 4.
```

## Restrições:

1 <= num <= 3999  
