# 로지스틱 회귀를 이용한 방법
# 구하고자 하는 것 : 광고를 듣고 그 사람이 적금을 넣었을지 예측
# 두개의 파일을 한번에 볼 수 있도록

import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('bank_marketing_simple.csv', sep=';')
df = pd.get_dummies(df, columns=['job','marital','education','default','housing','loan','contact','day','month','poutcome'])

dd = pd.read_csv('bank_marketing_full.csv', sep=';')
dd = pd.get_dummies(dd, columns=['job','marital','education','default','housing','loan','contact','day','month','poutcome'])

train = df.sample(frac=0.8, random_state=200)
test = df.drop(train.index)

train_y = train["y"]
del train["y"]
train_x = train

test_y = test["y"]
del test["y"]
test_x = test

# 로지스틱 회귀 실행
logistic = LogisticRegression(solver='newton-cg')
# solver= 'newton-cg' : 알고리즘으로 바꾼다는 의미(데이터를 처리할 수 있는 것이 한계가 있기 때문에 좀 더 많이 처리할 수 있도록 사용하는것)
logistic.fit(train_x, train_y)

score = logistic.score(test_x, test_y)
print(score)
