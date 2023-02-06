import requests
import json
import pandas as pd


header_csv = ["Rodada", "Mandante", "Placar Mandante", "Visitante", "Placar Visitante"]

headers = {
    'authority': 'api.globoesporte.globo.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://ge.globo.com',
    'referer': 'https://ge.globo.com/futebol/brasileirao-serie-b/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
writer = pd.ExcelWriter('tabela_serieB.xlsx')
total_jogos = []
for numero_rodada in range(1, 39, 1):
    response = requests.get(
        f'https://api.globoesporte.globo.com/tabela/009b5a68-dd09-46b8-95b3-293a2d494366/fase/brasileiro-serie-b-2022-fase-unica/rodada/{numero_rodada}/jogos/',
        headers=headers,
    )

    lista_response = json.loads(response.text)
    rodada = numero_rodada
    dados_jogos = []
    for id_partida in range(10):
        mandante = lista_response[id_partida]['equipes']['mandante']['nome_popular']
        visitante = lista_response[id_partida]['equipes']['visitante']['nome_popular']
        placar_mandante = lista_response[id_partida]['placar_oficial_mandante']
        placar_visitante = lista_response[id_partida]['placar_oficial_visitante']

        jogo = {"rodada": rodada, "mandante": mandante, "visitante": visitante, "placar_mandante": placar_mandante, "placar_visitante": placar_visitante}
        dados_jogos.append(jogo)
        df_rodadas = pd.DataFrame(data=dados_jogos)

    total_jogos.append(dados_jogos)
    df_rodadas.to_excel(writer, sheet_name=f'Rodada {numero_rodada}')
writer.save()

rodadas = mandantes = visitantes = placares_mand = placares_visit = []
