# Importar bibliotecas
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates

# Leer los datos
df = pd.read_csv('argentina_prestamos.csv', na_values='..')
print(df.iloc[0, :])
# Reemplazar la columna 'Value' con tus datos

# Imprimir la primera columna



# Transformar los datos
df = df.melt(id_vars=['Country Name', 'Country Code', 'Series Name', 'Series Code', ], 
             var_name='Date',  
             value_name='Value')
df['Date'] = df['Date'].str.slice(0, 6)  # Extraer el trimestre y el año
df['Date'] = pd.to_datetime(df['Date'])  # Convertir a datetime

# Crear figura y eje
fig, ax = plt.subplots(figsize=(12,8))

# Crear gráficos de línea para cada serie
for series in df['Series Name'].unique():
    data = df[df['Series Name'] == series]
    sns.lineplot(ax=ax, x=data['Date'], y=data['Value'], label=series)

# Ajustar formato del eje x
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

# Añadir título, leyenda y etiquetas
ax.set_title('Préstamos multilaterales de Venezuela')
ax.legend()
ax.set_xlabel('Fecha')
ax.set_ylabel('Total dinero en Notacion Cientifica')

# Mostrar figura
plt.show()
