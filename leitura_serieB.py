import pandas as pd


all_sheets = pd.read_excel('tabela_serieB.xlsx', sheet_name=None)


for key, value in all_sheets.items():
    print(value)
    print()

