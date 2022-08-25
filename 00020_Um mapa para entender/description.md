No exercício anterior fizemos um mapeamento usando `for...in`. Em Python, temos outras maneiras de fazer isso, as compreensões de lista! :star_struck:

Vamos ver como funcionam, se de uma lista de strings quiséssemos obter uma lista com os comprimentos de cada uma, poderíamos definir:


``` python
def comprimento(palavras):
  longo = []
  for palavra in palavras:
    list.append(longo, len(palavra))
  return longo
```

No entanto, também podemos fazer dessa maneira usando as compreensões de listas:

``` python
def comprimento(palavras):
  return [len(palavra) for palavra in palavras]
```

> Redefina a função `meses` para fazer o mesmo de antes, mas usando compreensões de listas.
