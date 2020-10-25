import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns

# 데이터 불러오기
df = pd.read_csv('seoul.csv')
lable_count = len(df['name'].unique())

# 데이터를 시각적으로 확인
# fit_reg=False 는 회귀선을 없애는 것, True 로 설정하면 각 데이터에 대한 회귀선이 생김
sns.lmplot('lat', 'lon', data=df, hue='name', fit_reg=False)
plt.show()

# 테스트 데이터 분리
train = df.sample(frac=0.8, random_state=200)
test = df.drop(train.index)

# KNN 구하기
knn = KNeighborsClassifier(n_neighbors=lable_count)
knn.fit(train[['lat', 'lon']], train['name'])
score = knn.score(test[['lat', 'lon']], test['name'])
print(score)

# 레이블 예측하기
guess = pd.DataFrame(columns=['lat', 'lon'])
guess.loc[0] = [37.502212, 127.113068]
print(knn.predict(guess))

# knn 은 한계가 있다는 것을 알아야함