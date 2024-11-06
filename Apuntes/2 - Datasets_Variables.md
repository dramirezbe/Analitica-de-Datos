# Datasets

## Dónde Encontrarlos

registry.opendata.aws

cloud.google.com/bigquery/public-data/

archive.ics.uci.edu/ml/datsets.php

www.kaggle.com

www.quandl.com/search

data.world

www.data.gov

data.worldbank.org

reddit.com/datasets

academictorrents.com

www.opengovpartnership.org/es/

www.datos.gov.co/browse

## Datos Estructurados vs No Estrucuturados

Datos no estructurados = Requiere un paso adicional de procesamiento (Audio, Imágenes, pdf, sensores)

Estructurados = Se pueden meter al modelo directamente o con un procesamiento mínimo

## Tipos de variables

### Cuantitativas

- Continua = Toma cualquier valor de un intervalo
- Discreta = Toma valores enteros, sin necesidad de un intervalo

### Cualitativas

- Ordinal = Caracteristicas con orden preestablecido
- Nominal = Cualidades cuyas categorías no tienen un nombre preestablecido

## Recomendación

Fundamentals of Data Visualization - Claus O. Wilke

## Tarea:

Investigar:
- Descriptores de datos (media, desviación estándar, varianza, mediana)
- Rangos intercuartiles
- Box Plots
- Normalización de datos



# Investigación:

## Descriptores de datos:
### Media: 

$$\mu = \frac{1}{n} \sum_{i=1}^{n} x_i$$
Representa el punto de equilibrio de la distribución y está influida por los valores extremos. Proporciona una medida de la tendencia general

### Desviación Estándar:

$$\sigma = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)^2}$$
Es una medida de variabilidad. Se utiliza para calcular la disperción en la que los puntos de datos individuales difieren de la media.

Una desviación baja indica que los puntos de datos están muy cerca de la media, mientras que una desviación alta muestra que los datos están dispersos en un rango mayor de valores.

Por ejemplo sirve mucho para saber la volatilidad del mercado.

### Varianza:

$$\sigma^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)^2$$
Cuanto más grande sea el valor de la varianza, más dispersos están los datos.
Y al revés, cuanto más pequeña sea el valor de la varianza, menos dispersión habrá en la serie de datos. Sin embargo, al 
interpretar la varianza hay que prestar atención con los valores atípicos (outliers), ya que pueden distorsionar el valor de la varianza.

### Mediana:

$$
M = 
\begin{cases} 
x_{\frac{n+1}{2}} & \text{si } n \text{ es impar} \\
\frac{x_{\frac{n}{2}} + x_{\frac{n}{2}+1}}{2} & \text{si } n \text{ es par}
\end{cases}
$$

Es el valor que se encuentra en el centro de los datos organizados de manera ascendente. Si los datos tienen una cantidad de muestras par, va a ser el promedio entre los dos valores adyacentes del centro de los datos, si es impar, es el valor del centro. 


## Rango Intercuartil:

Se debe de hallar el tercer y el primer cuartil:

- Para hallar cuartiles se debe ordenar los datos de manera ascendente

- El primer cuartil($Q_1$) es el valor que está en el 25% de los datos.
- El segundo cuartil($Q_2$) es el valor que está en el 50% de los datos.
- El tercer cuartil($Q_3$) es el valor que está en el 75% de los datos.
- El cuarto cuartil($Q_4$) es el valor máximo de los datos.

el rango intercuartil es:
$$
IQR = Q_3 - Q_1
$$

Es un representador estadístico muy robusto, ya que apenas cambia su valor
por valores atípicos(outliers)

## Boxplot:





