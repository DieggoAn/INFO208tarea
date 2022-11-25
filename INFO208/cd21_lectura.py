# Para instalar, indicar en terminal:
# pip install pandas
import pandas as pd
# Para instalar, indicar en terminal:
# pip install seaborn
import seaborn as sns
# Para instalar, indicar en terminal:
# pip install matplotlib
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
sns.set_palette('Set2')

# Lectura de datos
# Dataframe
credibilidad = pd.read_csv("/home/diego/Desktop/INFO208/credibilidad.csv", encoding="utf-8", sep=",")
variables = credibilidad.columns
# Columnas 0-2: datos del estudiantes y el nivel de SRL (target, variable dependiente)
# Columnas 3- : respuestas de la encuesta
print(credibilidad[variables[3]])
print(credibilidad.columns)

sns.scatterplot(y=credibilidad[variables[3]], x=credibilidad[variables[4]], hue=credibilidad[variables[2]])
plt.show()
