from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.linear_model import LinearRegression
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

fetch_data = fetch_california_housing()

fetch = pd.DataFrame(data=fetch_data.data, columns=fetch_data.feature_names)
fetch['target'] = fetch_data.target

train = fetch.sample(frac=0.8, random_state=200)
test = fetch.drop(train.index)

# 캘리포니아 회귀 분석 실행하기
mlr = LinearRegression()
mlr.fit(train[["MedInc","HouseAge","AveRooms","AveBedrms","Population","AveOccup","Latitude","Longitude"]], train['target'])
print(mlr.intercept_)  # mlr.intercept_ 는 절편을 의미한다
print(mlr.coef_)  # mlr.coef_ 는 계수를 의미한다

sum_difference = 0
for i, row in test.iterrows():
    estimate = row["MedInc"] * mlr.coef_[0] + row["HouseAge"] * mlr.coef_[1] + row["AveRooms"] * mlr.coef_[2] + row["AveBedrms"] * mlr.coef_[3] + \
               row["Population"] * mlr.coef_[4] + row["AveOccup"] * mlr.coef_[5] + row["Latitude"] * mlr.coef_[6] + row["Longitude"] * mlr.coef_[7] + \
               + mlr.intercept_

    # 최적의 변수 찾아내기
    difference = abs(row["target"] - estimate)
    sum_difference += difference

print(difference)

scatter_matrix(fetch.drop(columns=["HouseAge","AveRooms","AveBedrms","Population","AveOccup","Latitude","Longitude"]))
plt.show()