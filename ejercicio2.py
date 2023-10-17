import pandas as pd
import os
import matplotlib.pyplot as plt
import yagmail

# Ruta al directorio que contiene los archivos Excel
directorio = 'C:/Users/Camilo/Documents/python'

# Crea un diccionario para almacenar los DataFrames
diccionario_dataframes = {}

# Recorre los archivos en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith('.xlsx'):
        # Construye la ruta completa al archivo
        ruta_completa = os.path.join(directorio, archivo)
        
        # Lee el archivo Excel
        df = pd.read_excel(ruta_completa)

df['Total_Ventas'] = df.iloc[:, 1:].sum(axis=1)

print (df['Total_Ventas'])

df = df.sort_values(by='Total_Ventas', ascending=False)

top_2_modelos = df.head(2)

plt.figure(figsize=(10, 6))
plt.bar(top_2_modelos['Modelo'], top_2_modelos['Total_Ventas'])
plt.xlabel('Modelo')
plt.ylabel('Total de Ventas')
plt.title('Los Dos Modelos Más Vendidos')
plt.xticks(rotation=45)
plt.tight_layout()

# Guarda el gráfico en un archivo
plt.savefig('grafico.png', bbox_inches='tight')

# Configura yagmail para enviar el correo
yag = yagmail.SMTP('tucorreo@gmail.com','tupassword')

# Envía el correo
yag.send(
    to='tucorreo@gmail.com',
    subject='Gráfico de los modelos más vendidos',
    contents='Adjunto encontrarás el gráfico de los modelos más vendidos.',
    attachments='grafico.png'
)

# Cierra la conexión de yagmail
yag.close()
