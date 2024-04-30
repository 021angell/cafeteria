import pandas as pd

# Dados dos pacientes
dados_pacientes = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Luiza', 'Carlos', 'Mariana', 'José', 'Laura', 'Paulo'],
    'Idade': [30, 45, 25, 60, 35, 50, 28, 42, 55, 33],
    'Sexo': ['M', 'F', 'M', 'F', 'F', 'M', 'F', 'M', 'F', 'M'],
    'Doença': ['Hipertensão', 'Diabetes', 'Asma', 'Artrite', 'Câncer', 'Obesidade', 'Enxaqueca', 'Hipertensão', 'Depressão', 'Asma']
}

# Criando o DataFrame
df_pacientes = pd.DataFrame(dados_pacientes)

# Definindo as prioridades
prioridades = ['Emergência', 'Muito urgente', 'Urgente', 'Pouco urgente', 'Não urgente']

# Atribuindo prioridades aos pacientes de acordo com a ordem predefinida
df_pacientes['Prioridade'] = pd.Categorical(df_pacientes.index.map(lambda x: prioridades[x % len(prioridades)]))

# Exibindo o DataFrame
print(df_pacientes)