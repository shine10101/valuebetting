import pandas as pd

def value(predictions):
    odds = predictions[['B365H', 'B365D', 'B365A']]
    implied_odds = 1/odds
    probability = predictions[['HWin', 'Draw', 'AWin']]
    value = pd.DataFrame(probability.values - implied_odds.values,columns={'Home Win', 'Draw', 'Away Win'})
    predictions['Max_Value'] = pd.DataFrame(value.max(axis=1))
    predictions['Max_Value_Result'] = pd.DataFrame(value.idxmax(axis=1))
    predictions = predictions.sort_values('Max_Value', ascending=False)
    return predictions
