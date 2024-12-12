# Reducción de dimensión

- Siempre se va a peder información, así sea poca, al reducir la dimensión.
- La Maldición de la dimensión: entre más dimensiones halla, nuestro modelo se va a demorar más.
- Si vamos a hacer clasificación, se debe tener 30 muestras por característica.

# PCA

Es encontrar el hiperplano tal que menos cambie la disperción(varianza) de los datos.

- Cuántas componentes estima PCA? Cuantas características tenga su base de datos. (Debe retener el 100% de varianza al sumar sus componentes)

## kPCA

Se usa un kernel. Cambia la forma de los datos, por lo que es dificil de reconstruir.


**Consulta:**

- En qué consisten las Eigen-faces.
 
- Qué kernel existen para calcular kPCA