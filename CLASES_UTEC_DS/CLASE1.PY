import pandas as pd
import numpy as np  # Sintaxis correcta para importar NumPy
import seaborn as sns
from pathlib import Path

data = {
    "nombre": ["Andres", "Alonso", "Fanny", "Yemeli", "Victor"],
    "Edad": [18, 18, 45, 22, 49],
    "Código": ["A1", "A2", "A3", "A4", "A5"],
    "SEXO": ["M", "M", "F", "F", "M"],
}



# Usa pd.read_csv para abrir archivos CSV desde una ruta

print()