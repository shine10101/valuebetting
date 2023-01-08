import pandas as pd

def get_links():
    season = '2223'
    refs = ['E0', 'E1', 'E2', 'E3', 'EC', 'SC0', 'SC1', 'SC2', 'SC3', 'D1', 'D2', 'I1', 'I2', 'F1', 'F2', 'SP1', 'SP2', 'N1', 'B1', 'T1', 'P1']
    data = []
    for league in refs:
        url = 'https://football-data.co.uk/mmz4281/' + season + '/' + league + '.csv'
        r = pd.read_csv(url,parse_dates=['Date'], date_parser=lambda x: pd.to_datetime(x, format='%d/%m/%Y'))
        data.append(r)

    return data

