from sklearn.datasets import load_boston
import pandas as pd
import statsmodels.formula.api as sm

boston_data = load_boston()

boston = pd.DataFrame(data=boston_data.data, columns=boston_data.feature_names)
boston['target'] = boston_data.target

train = boston.sample(frac=0.8, random_state=200)
test = boston.drop(train.index)

result = sm.ols(formula = 'target ~ CRIM + ZN + CHAS + NOX + RM + DIS + RAD + TAX + PTRATIO + B + LSTAT', data = train).fit() #formula 는 R에 대한 문법

print(result.summary())

sum_difference = 0
for i, row in test.iterrows():
    params = result.params
    r_estimate = row['CRIM'] * params['CRIM']  + row['ZN'] * params['ZN'] + row['CHAS'] * params['CHAS'] + row['NOX'] * params['NOX'] \
                 + row['RM'] * params['RM'] + row['DIS'] * params['DIS'] + row['RAD'] * params['RAD'] + row['TAX'] * params['TAX'] \
                 + row['PTRATIO'] * params['PTRATIO'] + row['B'] * params['B'] + row['LSTAT'] * params['LSTAT'] + params['Intercept']

    difference = abs(row['target'] - r_estimate)
    sum_difference += difference

print(sum_difference)