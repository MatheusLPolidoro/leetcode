# Mediana de duas matrizes classificadas

Dadas duas matrizes classificadas nums1 e nums2 de tamanho m e n respectivamente, retorne a mediana das duas matrizes classificadas.  

A complexidade geral do tempo de execução deve ser O(log (m+n)).

## Exemplos:
```
Entrada: nums1 = [1,3], nums2 = [2]
Saída: 2.00000
Explicação: matriz mesclada = [1,2,3] e mediana é 2.
```
```
Entrada: nums1 = [1,2], nums2 = [3,4]
Saída: 2.50000
Explicação: matriz mesclada = [1,2,3,4] e mediana é (2 + 3) / 2 = 2,5.
``` 

## Restrições:

nums1.length == m  
nums2.length == n  
0 <= m <= 1000  
0 <= n <= 1000  
1 <= m + n <= 2000  
-106 <= nums1[i], nums2[i] <= 106  