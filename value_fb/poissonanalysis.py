import pandas as pd


def analysis(Train, test, teams):

    fix_train = Train[['HomeTeam', 'AwayTeam']]
    home_form = []
    away_form = []
    # calculate home and away strengths
    for team in teams[0]:
        team = teams[0][0]
        team_games = Train[(Train['HomeTeam']==team) | (Train['AwayTeam']==team)]
        HF = dict()
        AF = dict()

        HF['GamesplayedH'] = len(Train[Train['HomeTeam']==team])
        HF['GoalsforH'] = sum(Train['FTHG'][Train['HomeTeam']==team])
        HF['AvggoalsforH'] = Train['FTHG'][Train['HomeTeam']==team].mean()
        HF['GoalsagainstH'] = sum(Train['FTAG'][Train['HomeTeam']==team])
        HF['AvggoalsagainstH'] = Train['FTAG'][Train['HomeTeam']==team].mean()

        AF['GamesplayedA'] = len(Train[Train['AwayTeam']==team])
        AF['GoalsforA'] = sum(Train['FTAG'][Train['AwayTeam']==team])
        AF['AvggoalsforA'] = Train['FTAG'][Train['AwayTeam']==team].mean()
        AF['GoalsagainstA'] = sum(Train['FTHG'][Train['AwayTeam']==team])
        AF['AvggoalsagainstA'] = Train['FTHG'][Train['AwayTeam']==team].mean()

        home_form.append(HF)
        away_form.append(AF)
