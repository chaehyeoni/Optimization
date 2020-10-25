from sklearn.datasets import load_boston
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import pandas as pd

# 데이터를 메모리에 불러오기
# load_boston : boston 에 있는 모든 집값 정보를 불러오는 함수
# DataFrame 은 pandas 에서 데이터를 처리하기 위한 기준
# target 은 데이터의 결과(y값)을 의미
boston_data = load_boston()

boston = pd.DataFrame(data=boston_data.data, columns=boston_data.feature_names)
boston['target'] = boston_data.target

# 데이터 분리하기 (데이터로 경향성을 예측할 때 검증이 필요)
train = boston.sample(frac=0.8, random_state=200)  # frac=0.8 는 80%정도의 데이터를 샘플링
test = boston.drop(train.index)

# 데이터의 경향성 파악하기 (scatter_matrix(boston)을 사용하면 matrix 형태로 데이터 간의 연관성을 파악 할 수 있음 -> 하지만 그래프가 복잡해서 한눈에 보기 힘들다.)
# boston.drop(scatter_matrix(boston.drop(columns=[]))을 사용하여 데이터를 제한해서(빼고) 한눈에 보기 쉽게 나타낸다.
scatter_matrix(boston.drop(columns=["B","RM","ZN","NOX","AGE","DIS","RAD","TAX","CHAS","INDUS","LSTAT","PTRATIO"]))
plt.show()