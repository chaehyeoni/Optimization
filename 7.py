import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import seaborn as sns

df = pd.read_csv('telecom_churn.csv')
sns.lmplot('tenure', 'MonthlyCharges', data=df, hue='Churn', fit_reg=False)
plt.show()

train = df.sample(frac=0.9, random_state=200)
test = df.drop(train.index)

logistic = LogisticRegression()
logistic.fit(train[['tenure', 'MonthlyCharges']], train['Churn'])
score = logistic.score(test[['tenure', 'MonthlyCharges']], test['Churn'])

print(score)

# 카테고리에 해당하는 데이터(숫자가 아닌 데이터)들은 회귀 분석이 불가능
# 따라서 회귀 분석을 하려면 숫자 데이터로 치환시켜야 함 (특정 값을 매겨서)
# 같은 카테고리인 경우 같은 값을 부여해야 의미가 있음
# 하나하나 값을 부여하기 힘들기 때문에 카테고리를 수치화 시키는 방법을 이용함 -> One hot encoding, Label Encoding
# Label Encoding : 카테고리가 있을 때 첫번째를 1, 두번째를 2, 이런방식으로 차례대로 설정함
# One hot encoding : 특정한 것에 1이라고 설정하고 나머지를 0이라고 설정함