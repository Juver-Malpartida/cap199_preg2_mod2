# Solucion

import pandas as pd
import requests
import zipfile
import io
import os

%cd /content/

# URL del archivo ZIP
zip_file_url = "https://github.com/robintux/Datasets4StackOverFlowQuestions/raw/master/Cancer_Pulmon.zip"

# Nombre del archivo zip local
zip_file_name = "Cancer_Pulmon.zip"

# Directorio de extracción
extract_dir = "./Cancer_Pulmon_data"

# Crear el directorio de extracción si no existe
os.makedirs(extract_dir, exist_ok=True)

# Descargar el archivo ZIP
response = requests.get(zip_file_url)
response.raise_for_status() # Lanza un error para códigos de estado HTTP incorrectos

# Guardar el archivo zip
with open(zip_file_name, "wb") as f:
    f.write(response.content)

# Extraer el contenido del archivo zip
with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

csv_file_path = os.path.join(extract_dir, 'Cancer_Pulmon.csv')
df = pd.read_csv(csv_file_path)
display(df.head())

# Eliminar el archivo zip descargado para limpiar
os.remove(zip_file_name)
# print(f"Archivo {zip_file_name} eliminado.")
