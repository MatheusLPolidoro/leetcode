# Correspondência de expressão regular

Dada uma string de entrada s e um padrão p, implemente correspondência de expressão regular com suporte para '.' e onde:  

'.' Corresponde a qualquer caractere único.  
'*' Corresponde a zero ou mais do elemento anterior.  
A correspondência deve abranger toda a string de entrada (não parcial).  

## Exemplos:
```
Entrada: s = "aa", p = "a"
Saída: falso
Explicação: "a" não corresponde à string inteira "aa".
```
```
Entrada: s = "aa", p = "a*"
Saída: verdadeiro
Explicação: '*' significa zero ou mais do elemento precedente, 'a'. Portanto, ao repetir 'a' uma vez, torna-se "aa".
```
```
Entrada: s = "ab", p = ".*"
Saída: verdadeiro
Explicação: ".*" significa "zero ou mais (*) de qualquer caractere (.)".
``` 

## Restrições:

1 <= s.length <= 20  
1 <= p.length  <= 20  
s contém apenas letras minúsculas em inglês.  
p contém apenas letras minúsculas do inglês, '.' e '*'.  
É garantido que para cada aparição do caractere '*', haverá um caractere anterior válido para corresponder.