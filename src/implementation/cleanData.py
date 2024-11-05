import pandas as pd


df = pd.read_excel('../data/data.xlsx')

# remove linhas em que a coluna Email não contem '@'
df = df[df['Email'].str.contains('@', na=False)]

# splita a coluna Email por '-' e pega o 2 campo
df['Email'] = df['Email'].str.split('-').str[2]

# splita a coluna Nome por ' ' e pega os dois primeiros campos
df['Nome'] = df['Nome'].str.split().str[:2].str.join(' ')

# Remove linhas com campos Nome ou Email nulos
df = df.dropna(subset=['Nome', 'Email'])

# Remove linhas onde a coluna Nome contém números
df = df[~df['Nome'].str.contains(r'\d', na=False)]

# Remove a primeira palavra do Nome se ela tiver 1 ou 2 caracteres
df['Nome'] = df['Nome'].apply(lambda x: ' '.join([word for word in x.split() if len(word) > 2]))

# Salvan o arquivo
df.to_excel('../../data.xlsx', index=False)

print(df)
