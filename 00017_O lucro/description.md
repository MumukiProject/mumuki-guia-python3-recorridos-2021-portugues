Ana, contadora de uma conhecida empresa :office:, tem dicionários para representar os balanços de cada mês e diferentes listas para armazená-los. Por exemplo:

``` python
#Em julho ela ganhou $50, em agosto ela perdeu $12, etc.
balancos_ultimo_semestre = [
    { "mes": "julho", "lucro": 50 },
    { "mes": "agosto", "lucro": -12 },
    { "mes": "setembro", "lucro": 1000 },
    { "mes": "outubro", "lucro": 300 },
    { "mes": "novembro", "lucro": 200 },
    { "mes": "dezembro", "lucro": 0 }
]

balancos_primeiro_trimestre = [
    { "mes": "janeiro", "lucro": 2 },
    { "mes": "fevereiro", "lucro": 10 },
    { "mes": "março", "lucro": -20 }
]
```

Dito isso, Ana precisa saber o lucro acumulado para um conjunto de balanços.

> Defina a função `lucro_total` que, dada uma lista de balanços qualquer, retorne a soma de todos eles:
>
``` python
ム lucro_total(balancos_ultimo_semestre)
1538
```
