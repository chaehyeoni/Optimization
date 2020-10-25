import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

# 데이터 초기화
data = [[7,1], [2,1], [4,2], [9,4], [10,5], [10,6], [11,5], [11,6], [15,3], [15,2], [16,4], [16,1]]

df = pd.DataFrame(columns=['x','y'], data=data)

distortions = []

# 클러스터 개수별 최저 거리 구하기
# 1부터 10까지 어느것이 최적인지 찾기 위해 범위를 정해줌 (수치는 고정해 줘야함)
# km.cluster_centers_ 는 중심점을 의미하고, euclidean 로 계산해준다.(x 증가량 y 증가량) -> 편하게 구할 수 있어 많이 사용하지만, 정확도가 좀 떨어진다는 단점이 있음.
for cluster in range(1, 10):
    km = KMeans(n_clusters=cluster).fit(df[['x','y']])
    # 중심점과 모든 좌표들간의 거리 (N:M)
    distance = cdist(df[['x','y']], km.cluster_centers_, 'euclidean')

    # 중심점-좌표간 거리 중 최저인 값
    # np.min 을 실행시키면 각 점별로 최소 중심점이 제일 가까운 점을 뽑아냄. (중심점과 최소거리인 애들을 추릴때 사용)
    min_distance = np.min(distance, axis=1)
    sum_distance = sum(min_distance)

    # 평균 최소거리의 합
    # df[['x','y']].shape[0] 은 len 으로 바꿔서 사용해도 됨.
    distortions.append(sum_distance / df[['x','y']].shape[0])

plt.plot(range(1, 10), distortions)
plt.show()

# KMeans 알고리즘은 세세하게 쪼개는 것이 아닌 적당히 쪼개는 것이 좋음