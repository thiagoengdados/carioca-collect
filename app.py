# %%
import requests
from bs4 import BeautifulSoup
from http import HTTPStatus
import pandas as pd 
import re  
import json
from extractJsonResultadosCarioca import extractJsonResultadoCarioca


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}

url='https://www.espn.com.br/futebol/time/resultados/_/id/819/liga/BRA.1/temporada/2024'

response = requests.get(url, headers=headers)

if response.status_code == HTTPStatus.OK:

    soup = BeautifulSoup(response.content, "html.parser")  

    tbodies = soup.find_all('tbody', class_='Table__TBODY')

    score_carioca = []
    datas_carioca = []
    score_carioca_final = []

    for tbody in tbodies:

        rows = tbody.find_all('tr', class_='Table__TR')
    
        for tr in rows:

            tds = tr.find_all('td')[0:4]

            # EXTRAIR RESULTADOS JOGOS
            for time_placar in tds:
                times_placar = time_placar.find_all('a')
                for i in times_placar:
                    score_carioca.append(i.text.strip())  

            # EXTRAIR DATAS DOS JOGOS PARA RESPECTIVOS RESULTADOS
            for data_jogo in tds:
                datas_jogos = data_jogo.find_all('div', class_='matchTeams')

                for i in datas_jogos:
                    datas_carioca.append(i.text.strip())  

else:
    print(f"Erro ao acessar a pagina. Codigo HTTP: {response.status_code == HTTPStatus.BAD_REQUEST}")
    
extractJsonResultadoCarioca(score_carioca, datas_carioca, score_carioca_final )

# Convertendo para DataFrame
df = pd.DataFrame(score_carioca_final)

# Exibindo a tabela corretamente
print(df)


