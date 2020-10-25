import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns

df = pd.read_csv('fruit_data_with_colors.csv')
lable_count = len(df['fruit_label'].unique())

# sns.lmplot('width', 'height', data=df, hue='fruit_name', fit_reg=False)
# plt.show()

train = df.sample(frac=0.8, random_state=200)
test = df.drop(train.index)

knn = KNeighborsClassifier(n_neighbors=lable_count)
knn.fit(train[['width', 'height', 'mass', 'color_score']], train['fruit_label'])
score = knn.score(test[['width', 'height', 'mass', 'color_score']], test['fruit_label'])
print(score)

# 앞선 방법들의 한계
# 특정 요소를 설명하는 데이터들의 평균적인 기준으로 판단
# 아웃라이어(평균에서 크게 벗어난) 데이터들이 있는 경우
# 모든 기준이 상대적인 기준으로 되어 있어 상태에 따라 어려움
# 특정 레이블로 분류하기 위해서는 결국 임계점이 필요함 (기준을 정하고 수치적인 결과가 나오도록)
# -> 회귀분석을 한 결과로 임계점을 정하면 됨
