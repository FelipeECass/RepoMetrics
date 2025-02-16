import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('github_top_1000.csv', encoding='ascii')

df['created_at'] = pd.to_datetime(df['created_at'], utc=True)
df['updated_at'] = pd.to_datetime(df['updated_at'], utc=True)

data_ref = pd.to_datetime('2025-02-16', utc=True)

df['idade_repositorio_anos'] = (data_ref - df['created_at']).dt.days / 365

df['dias_desde_atualizacao'] = (data_ref - df['updated_at']).dt.days

df['taxa_issues_fechadas'] = df.apply(lambda row: row['closed_issues'] / row['total_issues'] if row['total_issues'] > 0 else None, axis=1)

# RQ 01: Idade dos repositórios
plt.figure(figsize=(8, 6))
sns.histplot(df['idade_repositorio_anos'], bins=30, kde=True, color='skyblue')
plt.title('RQ 01: Idade dos Repositórios (anos)')
plt.xlabel('Idade (anos)')
plt.ylabel('Número de Repositórios')
plt.tight_layout()
plt.savefig('visualizacao_rq01.png')
plt.close()

# RQ 02: Pull requests aceitos
plt.figure(figsize=(8, 6))
sns.histplot(df['pull_requests_accepted'], bins=30, kde=True, color='salmon')
plt.title('RQ 02: Total de Pull Requests Aceitos')
plt.xlabel('Pull Requests Aceitos')
plt.ylabel('Número de Repositórios')
plt.tight_layout()
plt.savefig('visualizacao_rq02.png')
plt.close()

# RQ 03: Releases
plt.figure(figsize=(8, 6))
sns.histplot(df['releases'], bins=30, kde=True, color='limegreen')
plt.title('RQ 03: Total de Releases')
plt.xlabel('Releases')
plt.ylabel('Número de Repositórios')
plt.tight_layout()
plt.savefig('visualizacao_rq03.png')
plt.close()

# RQ 04: Dias desde a última atualização
plt.figure(figsize=(8, 6))
sns.histplot(df['dias_desde_atualizacao'], bins=30, kde=True, color='violet')
plt.title('RQ 04: Dias desde a Última Atualização')
plt.xlabel('Dias desde atualização')
plt.ylabel('Número de Repositórios')
plt.tight_layout()
plt.savefig('visualizacao_rq04.png')
plt.close()

# RQ 05: Distribuição de Linguagens Primárias
plt.figure(figsize=(8, 6))
language_counts = df['primary_language'].value_counts(dropna=False)
sns.barplot(x=language_counts.values, y=language_counts.index, palette='pastel')
plt.title('RQ 05: Distribuição de Linguagens Primárias')
plt.xlabel('Número de Repositórios')
plt.ylabel('Linguagem Primária')
plt.tight_layout()
plt.savefig('visualizacao_rq05.png')
plt.close()

# RQ 06: Razão de issues fechadas
plt.figure(figsize=(8, 6))
sns.histplot(df['taxa_issues_fechadas'].dropna(), bins=30, kde=True, color='orange')
plt.title('RQ 06: Razão de Issues Fechadas em Relação ao Total')
plt.xlabel('Taxa de Issues Fechadas')
plt.ylabel('Número de Repositórios')
plt.tight_layout()
plt.savefig('visualizacao_rq06.png')
plt.close()
