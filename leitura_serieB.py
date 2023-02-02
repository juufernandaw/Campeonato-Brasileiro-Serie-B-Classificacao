# import module
import openpyxl

# load excel with its path
wrkbk = openpyxl.load_workbook("tabela_serieB.xlsx")
todas_rodadas = []
sh = wrkbk.active
cont = -1
for sh in wrkbk.worksheets:
    uma_rodada = []
    cont += 1
    for i in range(2, sh.max_row + 1):

        rodada = sh.cell(row=i, column=2).value
        mandante = sh.cell(row=i, column=3).value
        visitante = sh.cell(row=i, column=4).value
        placar_mandante = int(sh.cell(row=i, column=5).value)
        placar_visitante = int(sh.cell(row=i, column=6).value)
        if placar_mandante == placar_visitante:     # se for empate
            total_pontos_mandante = total_pontos_visitante = 1
        elif placar_mandante > placar_visitante:    # se o mandante vencer
            total_pontos_mandante = 3
            total_pontos_visitante = 0
        else:   # se o mandante perder
            total_pontos_mandante = 0
            total_pontos_visitante = 3
        if cont > 0:
            saldo_mandante = next(item["saldo_gols"] for item in todas_rodadas[cont-1] if item["time"] == mandante)
            saldo_visitante = next(item["saldo_gols"] for item in todas_rodadas[cont-1] if item["time"] == visitante)
            gols_pro_mandante = next(item["gols_pro"] for item in todas_rodadas[cont-1] if item["time"] == mandante)
            gols_pro_visitante = next(item["gols_pro"] for item in todas_rodadas[cont-1] if item["time"] == visitante)
            gols_contra_mandante = next(item["gols_contra"] for item in todas_rodadas[cont-1] if item["time"] == mandante)
            gols_contra_visitante = next(item["gols_contra"] for item in todas_rodadas[cont-1] if item["time"] == visitante)
            pontos_mandante = next(item["total_pontos"] for item in todas_rodadas[cont-1] if item["time"] == mandante)
            pontos_visitante = next(item["total_pontos"] for item in todas_rodadas[cont-1] if item["time"] == visitante)
        else:
            saldo_mandante = placar_mandante-placar_visitante
            saldo_visitante = placar_visitante-placar_mandante
            pontos_mandante = pontos_visitante = gols_pro_mandante = gols_pro_visitante = gols_contra_mandante = gols_contra_visitante = 0
        classificacao_mandante = {'time': mandante, 'total_pontos': pontos_mandante+total_pontos_mandante, 'gols_pro': gols_pro_mandante+placar_mandante, 'gols_contra': gols_contra_mandante+placar_visitante, 'saldo_gols': saldo_mandante-placar_visitante}
        classificacao_visitante = {'time': visitante, 'total_pontos': pontos_visitante+total_pontos_visitante, 'gols_pro': gols_pro_visitante+placar_visitante, 'gols_contra': gols_contra_visitante+placar_mandante, 'saldo_gols': saldo_visitante-placar_mandante}
        uma_rodada.append(classificacao_visitante)
        uma_rodada.append(classificacao_mandante)
    todas_rodadas.append(uma_rodada)

