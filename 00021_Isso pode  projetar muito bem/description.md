Ana faz muitas projeções sobre os balanços de sua empresa, então dissemos a ela que poderíamos dar uma ajuda agora que sabemos mapear. O que ela quer fazer é ver quais seriam os lucros em um balanço se todos eles estivessem em dobro :moneybag:. Por exemplo:

``` python
ム balanços_ultimo_semestre = [
    { "mes": "julho", "lucro": 50 },
    { "mes": "agosto", "lucro": -12 },
    { "mes": "setembro", "lucro": 1000 },
    { "mes": "outubro", "lucro": 300 },
    { "mes": "novembro", "lucro": 200 },
    { "mes": "dezembro", "lucro": 0 }
]

]

ムdobro_do_lucro(balanços_ultimo_semestre)
[100, -24, 2000, 600, 400, 0]
```

Como você verá, se os lucros forem negativos agora eles serão duas vezes negativos! :chart_with_downwards_trend:

> Defina a função `dobro_do_lucro`. Você pode usar `for...in` como compreensão de listas, o que você preferir.  :relaxed:
