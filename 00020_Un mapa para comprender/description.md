En el ejercicio anterior hicimos un mapeo utilizando `for...in`. En Python contamos con otras formas de hacer eso, ¡las listas por comprensión! :star_struck:

Veamos cómo funcionan, si a partir de una lista de strings quisieramos obtener una lista con los largos de cada uno, podríamos definir:

``` python
def largos(palabras):
  largos = []
  for palabra in palabras:
    list.append(largos, len(palabra))
  return largos
```

Sin embargo, también podríamos hacerlo de esta manera utilizando listas por comprensión:

``` python
def largos(palabras):
  return [len(palabra) for palabra in palabras]
```

> Redefiní la función `meses` para que haga lo mismo que antes pero utilizando listas por comprensión. 