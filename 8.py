# 특정 속성의 영향을 줄이기 위해서는  one hot encoding 을 사용해야함
# pandas 에서 one hot encoding 을 사용하려면 category 데이터여야 함

# dle df[" "] -> 불필요한 데이터 지우는 방법
# df = pd.get_dummies(df) -> one hot encoding 하는 방법

# 모르는 데이터 분석하는 방법
# 목표 값 설정
# 2개의 카테고리를 지닌 경우 -> Logistic 회귀
# 2개 이상의 카테고리를 지닌 경우 -> KNN
# 속성들에 의해 변화가 되는 수치가 있는 경우 -> Linear Regression

# KNN 을 사용한 방법
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('sharing_bike_train.csv')

# 엑셀에 나와있는 데이터는 사람이 보기 편한 형태로 컴퓨터가 처리할 수 있는 형태가 아니기 때문에 처리하기 위해 년,월,일,시간으로 바꾸는 코드 (보여주기 위한 데이터들)
df["year"] = pd.to_datetime(df["datetime"]).dt.year
df["month"] = pd.to_datetime(df["datetime"]).dt.month
df["day"] = pd.to_datetime(df["datetime"]).dt.day
df["hour"] = pd.to_datetime(df["datetime"]).dt.hour
df["weekday"] = pd.to_datetime(df["datetime"]).dt.weekday

# 날씨에 영향을 끼치지 않을 것 같은 불필요한 속성 제거
del df["datetime"]
del df["casual"]
del df["registered"]
del df["count"]

# One Hot Encoding 하기
df["year"] = df["year"].astype("category")
df["month"] = df["month"].astype("category")
df["day"] = df["day"].astype("category")
df["hour"] = df["hour"].astype("category")
df["weekday"] = df["weekday"].astype("category")
df["season"] = df["season"].astype("category")

df = pd.get_dummies(df)

print(df)
# 모든 카테고리를 가지고 종류_숫자로 정리해줌
print(df.shape)

# 테스트 데이터 분리 (학습용 데이터와 검증용 데이터를 분리하기 위해)
# train 은 내 생각, 내가 집어넣은 데이터가 딱 맞아 떨어지는 것이 오버피팅.. 따로 검증된 데이터를 집어넣으면 맞추지 못함
# 오버피팅(데이터가 딱 맞아 떨어지는 것), 언더피팅(데이터를 너무 맞추지 못하는 것) -> 최적화를 생기부에 넣었으면 공부하기..**
train = df.sample(frac=0.8, random_state=200)  # 랜덤값을 200만큼 설정하고 80%의 일부 데이터들을 추출하는 것
test = df.drop(train.index)  # 추출한 80% 데이터가 아닌 나머지 20%을 테스트에다가 넣는것

train_y = train["weather"]
del train["weather"]
train_x = train

test_y = test["weather"]
del test["weather"]
test_x = test

# KNN 으로 분석하기
knn = KNeighborsClassifier(n_neighbors=2)  # 자기 주변에 있는 데이터 2개를 확인해서 위치를 확인하는 것 (눈치보는 방식) / 값을 바꾸면서 테스트해봐야함
knn.fit(train_x, train_y)
score = knn.score(test_x, test_y)
print(score)

