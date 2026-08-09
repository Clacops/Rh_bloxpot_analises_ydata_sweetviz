import pandas as pd
import numpy as np

# Criando um DataFrame de exemplo simulando dados de RH
np.random.seed(42)
departamentos = ['TI', 'Recursos Humanos', 'Financeiro', 'Marketing', 'Operações']

dados_rh = {
    'Departamento': np.random.choice(departamentos, size=200),
    'Salario': np.random.normal(loc=5000, scale=1500, size=200).clip(2000, 15000),
    'Horas_Trabalhadas': np.random.randint(140, 220, size=200)
}

df_rh = pd.DataFrame(dados_rh)

# Visualizando as primeiras linhas
df_rh.head()