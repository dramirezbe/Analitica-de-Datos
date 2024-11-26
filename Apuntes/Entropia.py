import numpy as np

# Base de datos
db = {"Edad": [15, 20, 25, 30, 35, 40, 45, 50], "Clase": [0, 0, 1, 1, 0, 1, 1, 0]}
cortes = [22.5, 32.5, 37.5, 47.5]

edad = db["Edad"]
clase = db["Clase"]

# Función para calcular la entropía
def calcular_entropia(sub_clase):
    if len(sub_clase) == 0:
        return 0  # Si el subconjunto está vacío, la entropía es 0
    _, counts = np.unique(sub_clase, return_counts=True)
    probs = counts / len(sub_clase)
    return -np.sum(probs * np.log2(probs))

# Bucle para calcular la entropía de cada corte
for corte in cortes:
    # Dividir en subconjuntos según el corte
    indices_up = [i for i, e in enumerate(edad) if e <= corte]
    indices_down = [i for i, e in enumerate(edad) if e > corte]

    clases_up = [clase[i] for i in indices_up]
    clases_down = [clase[i] for i in indices_down]
    
    # Calcular entropías de los subconjuntos
    entropia_up = calcular_entropia(clases_up)
    entropia_down = calcular_entropia(clases_down)
    
    # Calcular entropía ponderada
    total = len(edad)
    entropia_total = (len(indices_up) / total) * entropia_up + (len(indices_down) / total) * entropia_down
    
    # Mostrar resultados
    print(f"Corte en {corte}:")
    print(f"  Subconjunto UP (<= {corte}): {clases_up}, Entropía: {entropia_up:.4f}")
    print(f"  Subconjunto DOWN (> {corte}): {clases_down}, Entropía: {entropia_down:.4f}")
    print(f"  Entropía total ponderada: {entropia_total:.4f}\n")
