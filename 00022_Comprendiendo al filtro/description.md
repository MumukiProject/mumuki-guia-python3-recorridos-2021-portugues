Así como podíamos hacer mapeos utilizando listas por comprensión, también podemos hacer filtrados. :open_hands:

Imaginemos que tenemos la función `mayores_a_5` que dada una lista de números nos retorna una nueva con aquellos que son mayores a 5:

``` python
def mayores_a_5(numeros):
  mayores = []
  for numero in numeros:
    if numero > 5:
      list.append(mayores, numero)
  return mayores
```

Otra manera de definirla sería haciendo:

``` python
def mayores_a_5(numeros):
  return [numero for numero in numeros if numero > 5]
```

> Redefiní la función `afortunados` para que haga lo mismo pero utilizando listas por comprensión.