import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns

# read_csv는 generator.csv을 읽어서 pandas에 바로 넣어주는 기능
# fit_reg=False 는 회귀선을 없애는 것, True 로 설정하면 각 데이터에 대한 회귀선이 생김
df = pd.read_csv('generator.csv')
sns.lmplot('RPM', 'VIBRATION', data=df, hue='STATUS', fit_reg=False)
plt.show()

# 테스트 데이터 분리
train = df.sample(frac=0.8,random_state=200)
test = df.drop(train.index)

# KNN 구하기
# RPM, VIBRATION 를 가지고 상태를 판단함
# score 는 채점을 하는 것 위에서는 train를 쓰고, 밑에는 test를 쓴 이유는 내가 테스트 한것과 train를 비교한다
# 결과가 1.0이기때문에 판단한것이 다 맞았다는 의미 (1이 100퍼센트를 의미)
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(train[['RPM', 'VIBRATION']], train['STATUS'])
score = knn.score(test[['RPM', 'VIBRATION']], test['STATUS'])

print(score)

# 레이블 예측하기
guess = pd.DataFrame(columns=['RPM', 'VIBRATION'])
guess.loc[0] = [800,200]
print(knn.predict(guess))

# 클러스터를 한 후에 색을 입히는 것이 아니라 색을 입히고 클러스터를 한다
# kmeans 와는 반대 방식으로 처리가 이루어짐.
