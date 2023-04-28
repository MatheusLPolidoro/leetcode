# Conversão em ziguezague

A string "PAYPALISHIRING" é escrita em um padrão em zigue-zague em um determinado número de linhas como este: 

```
P   A   H   N
A P L S I I G
Y   I   R
```

E então leia linha por linha: "PAHNAPLSIIGYIR"

Escreva o código que pegará uma string e fará essa conversão dado um número de linhas:

```
string convert(string s, int numRows);
```
## Exemplos:
```
Entrada: s = "PAYPALISHIRING", numRows = 3
Saída: "PAHNAPLSIIGYIR"
```
```
Entrada: s = "PAYPALISHIRING", numRows = 4
Saída: "PINALSIGYAHRPI"
Explicação:
P     I    N
A   L S  I G
Y A   H R
P     I
```
```
Entrada: s = "A", numRows = 1
Saída: "A"
``` 

## Restrições:

1 <= s.length <= 1000  
s consiste em letras inglesas (minúsculas e maiúsculas), ',' e '.'.  
1 <= numRows <= 1000
