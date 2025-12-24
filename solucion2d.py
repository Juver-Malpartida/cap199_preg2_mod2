# Solucion
import matplotlib.pyplot as plt
import seaborn as sns

# Variables para los boxplots
variables_to_plot = ['age', 'bmi', 'cholesterol_level']

# Crear una figura y un conjunto de subplots
fig, axes = plt.subplots(1, len(variables_to_plot), figsize=(20, 7))

# Iterar sobre las variables y crear un boxplot para cada una
for i, var in enumerate(variables_to_plot):
    sns.boxplot(y=df[var], ax=axes[i], color='lightgreen')
    axes[i].set_title(f'Boxplot de {var.replace("_", " ").title()}', fontsize=14)
    axes[i].set_ylabel(var.replace("_", " ").title(), fontsize=12)
    axes[i].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
