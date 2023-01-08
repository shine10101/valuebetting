import pandas as pd


def analysis(Train, test, teams):

    home_form=[]
    away_form=[]
    # calculate home and away strengths
    for team in teams[0]:
        HF = []
        AF = []

        HF.append(len(Train[Train['HomeTeam']==team]))
        HF.append(sum(Train['FTHG'][Train['HomeTeam']==team]))
        HF.append(Train['FTHG'][Train['HomeTeam']==team].mean())
        HF.append(sum(Train['FTAG'][Train['HomeTeam']==team]))
        HF.append(Train['FTAG'][Train['HomeTeam']==team].mean())

        AF.append(len(Train[Train['AwayTeam']==team]))
        AF.append(sum(Train['FTAG'][Train['AwayTeam']==team]))
        AF.append(Train['FTAG'][Train['AwayTeam']==team].mean())
        AF.append(sum(Train['FTHG'][Train['AwayTeam']==team]))
        AF.append(Train['FTHG'][Train['AwayTeam']==team].mean())

        home_form.append(HF)
        away_form.append(AF)

    home_form = pd.DataFrame(home_form, columns=['GamesplayedH', 'GoalsforH', 'AvggoalsforH', 'GoalsagainstH', 'AvggoalsagainstH'])
    away_form = pd.DataFrame(away_form, columns=['GamesplayedA', 'GoalsforA', 'AvggoalsforA', 'GoalsagainstA', 'AvggoalsagainstA'])

    median_avg_H = home_form.median()
    median_avg_A = away_form.median()

    HomeAtkStr = home_form['AvggoalsforH'] / median_avg_H['AvggoalsforH']
    HomeDefStr = home_form['AvggoalsagainstH'] / median_avg_H['AvggoalsagainstH']
    AwayAtkStr = away_form['AvggoalsforA'] / median_avg_A['AvggoalsforA']
    AwayDefStr = away_form['AvggoalsagainstA'] / median_avg_A['AvggoalsagainstA']

    team_strength = pd.concat([HomeAtkStr, HomeDefStr, AwayAtkStr, AwayDefStr], axis = 1)

    return team_strength