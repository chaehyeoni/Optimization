# clustering classification 의 차이점
# 이를 이용한 알고리즘에는 무엇이 있는지  (k-mean 알고리즘에서 k가 의미하는것은 갯수)
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 초기화
data = [[7,1], [2,1], [4,2], [9,4], [10,5], [10,6], [11,5], [11,6], [15,3], [15,2], [16,4], [16,1]]

df = pd.DataFrame(columns=['x','y'], data=data)

# 데이터 clustering 하기
km = KMeans(n_clusters=3).fit(df[['x','y']])

# 결과 출력하기
df['cluster_id'] = km.labels_

sns.lmplot('x', 'y', data=df, hue='cluster_id', fit_reg=False)
plt.show()
