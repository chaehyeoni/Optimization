import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import seaborn as sns

# 데이터 로드 & 데이터의 결 확인
df = pd.read_csv('breast_cancer.csv')
sns.lmplot('radius_mean', 'smoothness_mean', data=df, hue='diagnosis', fit_reg=False)
plt.show()

train = df.sample(frac=0.8, random_state=200)
test = df.drop(train.index)

# Logistic Regression 진행
logistic = LogisticRegression(solver="newton-cg")
logistic.fit(train[["radius_mean", "texture_mean", "perimeter_mean", "area_mean",
                    "smoothness_mean", "compactness_mean", "concavity_mean", "concave points_mean",
                    "symmetry_mean", "fractal_dimension_mean", "radius_se", "texture_se", "perimeter_se,area_se",
                    "smoothness_se", "compactness_se", "concavity_se", "concave points_se", "symmetry_se",
                    "fractal_dimension_se", "radius_worst", "texture_worst", "perimeter_worst", "area_worst",
                    "smoothness_worst", "compactness_worst", "concavity_worst", "concave points_worst",
                    "symmetry_worst", "fractal_dimension_worst"]],
             train['diagnosis'])

score = logistic.score(test[["radius_mean", "texture_mean", "perimeter_mean", "area_mean",
                             "smoothness_mean", "compactness_mean", "concavity_mean", "concave points_mean",
                             "symmetry_mean", "fractal_dimension_mean", "radius_se", "texture_se",
                             "perimeter_se,area_se",
                             "smoothness_se", "compactness_se", "concavity_se", "concave points_se", "symmetry_se",
                             "fractal_dimension_se", "radius_worst", "texture_worst", "perimeter_worst", "area_worst",
                             "smoothness_worst", "compactness_worst", "concavity_worst", "concave points_worst",
                             "symmetry_worst", "fractal_dimension_worst"]],
                       test["diagnosis"])

print(score)