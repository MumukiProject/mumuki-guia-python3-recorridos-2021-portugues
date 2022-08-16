¿Sabes cuántos meses tienen 28 días? :thinking:

¡Todos! :stuck_out_tongue_winking_eye:

Fuera del mal chiste, algunos meses son más largos que otros, es por eso que queremos saber de una lista de balances, cuáles corresponden a meses largos. Los meses largos son los que tienen 31 días. Veamos un ejemplo:

``` python
ム balances_primer_trimestre = [
    { "mes": "enero", "ganancia": 2 }, 
    { "mes": "febrero", "ganancia": 10 }, 
    { "mes": "marzo", "ganancia": -20 }
]

ム balances_de_meses_largos(balances_primer_trimestre)
[{ "mes": "enero", "ganancia": 2 }, { "mes": "marzo", "ganancia": -20 }]
```

> Definí la función `balances_de_meses_largos` que funciona como te mostramos arriba. Podés utilizar `for...in` o listas por comprensión. En ambos casos te va a ser útil el operador `in`. 