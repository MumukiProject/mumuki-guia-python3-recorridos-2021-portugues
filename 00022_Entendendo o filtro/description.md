Assim como podemos fazer mapeamento usando compreensões de lista, também podemos fazer filtros. :open_hands:

Vamos imaginar que temos a função `maiores_que_5`  que, dada uma lista de números, retorna uma nova com aqueles maiores que 5:

``` python
def maiores_que_5(numeros):
  maiores = []
  for numero in numeros:
    if numero > 5:
      list.append(maiores, numero)
  return maiores
```

Outra maneira de definir isso seria fazendo:

``` python
def maiores_que_5(numeros):
  return [numero for numero in numeros if numero > 5]
```

> Redefina a função `sortudo` para fazer a mesma coisa, mas usando compreensões de lista.
