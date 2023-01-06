import requests
import json
import csv


dados_jogos = []
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

for numero_rodada in range(1, 39, 1):
    response = requests.get(
        f'https://api.globoesporte.globo.com/tabela/009b5a68-dd09-46b8-95b3-293a2d494366/fase/brasileiro-serie-b-2022-fase-unica/rodada/{numero_rodada}/jogos/',
        headers=headers,
    )

    lista_response = json.loads(response.text)
    rodada = numero_rodada
    mandante = lista_response[0]['equipes']['mandante']['nome_popular']
    visitante = lista_response[0]['equipes']['visitante']['nome_popular']
    placar_mandante = lista_response[0]['placar_oficial_mandante']
    placar_visitante = lista_response[0]['placar_oficial_visitante']

    jogo = [rodada, mandante, visitante, placar_mandante, placar_visitante]
    dados_jogos.append(jogo)

with open('serie_b.csv', 'w', encoding='UTF8', newline='') as texto:
    writer = csv.writer(texto)
    writer.writerow(header_csv)
    writer.writerows(dados_jogos)
