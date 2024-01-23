import pandas as pd
from sqlalchemy import create_engine

# Configuração da conexão
dados_conexao = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=COLOQUE o SERVIDOR AQUI;"
    "Database=NOME DO BANCO DE DADOS AQUI;"
    'UID=LOGIN;'
    'PWD=SENHA'
)

# Criar uma engine usando SQLAlchemy
engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(dados_conexao))
print("Conexão bem sucedida")

# Executar a consulta SQL e criar um DataFrame
sql_query = pd.read_sql_query("""Select * from Vendas Where ValorTotal > 500.00""", engine)
df = pd.DataFrame(sql_query)

# Adicionar formatação para a coluna ValorTotal
df['ValorTotal'] = df['ValorTotal'].map('R${:.2f}'.format)

# Remover a coluna 'QuantidadeVendida'
df = df.drop(columns=['QuantidadeVendida'])

# Salvar o DataFrame como um arquivo CSV
if not df.empty:
    df.to_csv(r'CAMINHO DE ONDE QUER SALVAR O ARQUIVO\nome do arquivo.csv', index=False)
    print("Arquivo CSV salvo com sucesso.")
else:
    print("DataFrame está vazio. Nenhum dado para salvar.")

