import pandas as pd
nome = {'animais':['unicornio','dragão','Fênix','leti'],
      'sexo': ['trans','hetero top','feminina','hetero top'],
      'peso': [80,200,65,300],
      'consumida por dia':[20,40,70,100]}
df = pd.DataFrame(nome)
print(df)

medias = df['peso'].mean()
print('a media dos pesos dos animais é',medias)


zoo_masculino_dataframe = df[df['sexo'] == 'hetero top']

# Exibindo o novo DataFrame
print(zoo_masculino_dataframe)