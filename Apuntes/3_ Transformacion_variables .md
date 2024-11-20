# Datos Perdidos

## Inputar Datos:
- Si hay datos perdidos, se debe de estimar el dato usando una manera inteligente (estadística(Moda, mediana, valores cercanos por ubicación, por esto, etc...))
- El mejor método de estimación de datos faltantes es un modelo de clasificación.


- 1ra opción eliminar datos faltantes y luego hacer el análisis. Si es exitoso, sirve el análisis



Contras:
- Fugas de información (data leakage)

## Transformación de variables numéricas:

- De numérica a categórica (consiste en agrupar los valores continuos en rangos)

Cómo se hace:

### Discretización de ancho uniforme:

$$w = \frac{max - min}{k}$$

Siendo k la cantidad de aprupaciones que quiero.

Por lo que los intervalos quedarían: $$min + w; min + 2w; ... ; min + (k-1)w$$


### Discretización no-supervisada de frecuencia uniforme:
- Que cada intervalo(rango) tenga el mismo número de valores.

### Discretización supervisada:
- Buscar la mejor partición tratando de que cada grupo tenga mayor "pureza"

Concepto de entropía, siendo pi la probabilidaa de cada evento. y c el número de eventos posibles:

$$E(S) = \sum_{i=1}^{c} p_i \log_2 p_i$$
