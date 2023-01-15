import pandas as pd
from value_fb import data_ingestion, poissonanalysis
import datetime

data = data_ingestion.get_links()

for league in data[0]:
    league = data[0]
    unique_dates = pd.DataFrame(league.Date.dt.strftime('%y-%m-%d').unique())
    unique_dates = [pd.to_datetime(t, format='%y-%m-%d') for t in unique_dates[0]]
    y = unique_dates[0] + datetime.timedelta(days=30)
    train_test_dates = [t for t in unique_dates if t > y]
    teams = pd.DataFrame(sorted(league.HomeTeam.unique()))
    results=pd.DataFrame()
    for day in train_test_dates[0]:
        day = train_test_dates[0]
        Train = league[(league['Date'] < day)]
        Test = league[(league['Date'] == day)]
        results.append(poissonanalysis.analysis(Train, Test, teams))

print('done')
