import requests
import pandas as pd
import time

# Defina seu token do GitHub (opcional, mas recomendado)
TOKEN = "TOKEN"
HEADERS = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

# Parâmetros básicos da API
BASE_URL = "https://api.github.com/search/repositories"
PARAMS = {
    "q": "stars:>0",
    "sort": "stars",
    "order": "desc",
    "per_page": 100
}

repositorios = []

# Coletar 1.000 repositórios (10 páginas)
for page in range(1, 11):
    print(f"Coletando página {page}...")
    PARAMS["page"] = page
    response = requests.get(BASE_URL, headers=HEADERS, params=PARAMS)

    if response.status_code != 200:
        print(f"Erro: {response.status_code}, {response.text}")
        break

    data = response.json()
    repositorios.extend(data["items"])

    # Evitar atingir limites da API
    time.sleep(2)

# Criar DataFrame com os dados coletados
df = pd.DataFrame(repositorios, columns=["id", "name", "full_name", "html_url", "stargazers_count", "language", "forks", "watchers", "created_at"])

# Salvar em CSV
df.to_csv("github_top_1000.csv", index=False)

print("Coleta finalizada e salva em 'github_top_1000.csv'.")
