import pandas as pd
from value_fb import data_ingestion, poissonanalysis
import datetime
from sklearn.metrics import classification_report

data = data_ingestion.get_links()

for league in data:
    league = data[0]
    unique_dates = pd.DataFrame(league.Date.dt.strftime('%y-%m-%d').unique())
    unique_dates = [pd.to_datetime(t, format='%y-%m-%d') for t in unique_dates[0]]
    y = unique_dates[0] + datetime.timedelta(days=30)
    train_test_dates = [t for t in unique_dates if t > y]
    teams = pd.DataFrame(sorted(league.HomeTeam.unique()))
    results=[]
    for day in train_test_dates:
        Train = league[(league['Date'] < day)]
        Test = league[(league['Date'] == day)]
        results.append(poissonanalysis.analysis(Train, Test, teams))

    output = pd.concat(results)
    # Calculate Overall prediction accuracy
    report = classification_report(output['FTR'], output['Pred_FTR'])

    # Calculate Prediction accuracy per team #TODO
    # Calculate Prediction accuracy BTTS #TODO
    # Calculate Prediction accuracy over/under 2.5 #TODO
print('done')
