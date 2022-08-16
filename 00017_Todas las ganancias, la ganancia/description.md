Ana, contadora de una conocida empresa :office:, tiene diccionarios para representar los balances de cada mes y distintas listas para guardarlos. Por ejemplo:

```python
#En julio ganó $50, en agosto perdió $12, etc.
balances_ultimo_semestre = [
	{ "mes": "julio", "ganancia": 50 }, 
	{ "mes": "agosto", "ganancia": -12 }, 
	{ "mes": "septiembre", "ganancia": 1000 }, 
	{ "mes": "octubre", "ganancia": 300 }, 
	{ "mes":  "noviembre", "ganancia": 200 }, 
	{ "mes": "diciembre", "ganancia": 0 }
]

balances_primer_trimestre = [
	{ "mes": "enero", "ganancia": 2 }, 
	{ "mes": "febrero", "ganancia": 10 }, 
	{ "mes": "marzo", "ganancia": -20 }
]
```

Dicho esto, Ana necesita saber la ganancia acumulada de un conjunto de balances.

> Definí la función `ganancia_total` que dado una lista de balances cualquiera nos devuelva la suma de todas:
>
```python
ム ganancia_total(balances_ultimo_semestre)
1538
```