import pandas as pd
from value_fb import data_ingestion, poissonanalysis, calculate_value
import datetime
from sklearn.metrics import classification_report
from multiprocessing import Pool
data, data_dct = data_ingestion.get_links()
fixtures = data_ingestion.get_fixtures()

print('stop')
def leagueanalysis(league):
    unique_dates = pd.DataFrame(league.Date.dt.strftime('%y-%m-%d').unique())
    unique_dates = [pd.to_datetime(t, format='%y-%m-%d') for t in unique_dates[0]]
    y = unique_dates[0] + datetime.timedelta(days=60)
    train_test_dates = [t for t in unique_dates if t > y]
    teams = pd.DataFrame(sorted(league.HomeTeam.unique()))
    results=[]
    for day in train_test_dates:
        Train = league[(league['Date'] < day)]
        Test = league[(league['Date'] == day)]
        results.append(poissonanalysis.analysis(Train, Test))

    output = pd.concat(results)
    # Calculate Overall prediction accuracy
    report = classification_report(output['FTR'], output['Pred_FTR'],output_dict=True)
    df_report = pd.DataFrame(report).transpose()
    df_report['league'] = league['Div'][0]

    return df_report

    # Calculate Prediction accuracy per team #TODO
    # Calculate Prediction accuracy BTTS #TODO
    # Calculate Prediction accuracy over/under 2.5 #TODO

def fixture_predictions(fixtures, data_dct):
    leagues = fixtures['Div'].unique()
    predictions=[]
    for league in leagues:
        try:
            league_fixtures = fixtures[fixtures['Div']==league]
            league_data = data_dct[league][0]
            predictions.append(poissonanalysis.analysis(league_data, league_fixtures))
        except:
            print(league)
            pass
    output = pd.concat(predictions)
    return output

if __name__ == '__main__':
    # with Pool(4) as pool:
    #     # df = pd.concat(pool.starmap(leagueanalysis, data))
    pred = fixture_predictions(fixtures, data_dct)
    pred = calculate_value.value(pred)
    pred.to_csv('predictions.csv')

    print('done')
