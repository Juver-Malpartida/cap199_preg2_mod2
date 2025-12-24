# Solucion

import matplotlib.pyplot as plt


fig, axes = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle('Cancer', fontsize=16, fontweight='bold')

# Histograma de la columna/variable : age
df['age'].hist(ax=axes[0, 0], bins=15, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Distribución de Edad')
axes[0, 0].set_xlabel('Edad')
axes[0, 0].set_ylabel('Frecuencia')

# Diagrama de tipo pie de la variable/columna : gender
gender_counts = df['gender'].value_counts()
axes[0, 1].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue'])
axes[0, 1].set_title('Distribución por Género')
axes[0, 1].axis('equal')

# Distribucion de paises (Columna : country) en un diagrama de barras
country_counts = df['country'].value_counts().head(10) # Mostrar los top 10 países
country_counts.plot(kind='bar', ax=axes[1, 0], color='lightgreen', edgecolor='black')
axes[1, 0].set_title('Distribución por País (Top 10)')
axes[1, 0].set_xlabel('País')
axes[1, 0].set_ylabel('Número de Casos')
axes[1, 0].tick_params(axis='x', rotation=45)

# Distribucion de la etapa del cancer (columna cancer_stage) en un diagrama de barras.
cancer_stage_counts = df['cancer_stage'].value_counts()
cancer_stage_counts.plot(kind='bar', ax=axes[1, 1], color='lightgray', edgecolor='black')
axes[1, 1].set_title('Distribución por Etapa del Cáncer')
axes[1, 1].set_xlabel('Etapa del Cáncer')
axes[1, 1].set_ylabel('Número de Casos')
axes[1, 1].tick_params(axis='x', rotation=0)

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajustar el diseño para evitar superposiciones
plt.show()
