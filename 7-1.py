import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

# 데이터 처리하기
df = pd.read_csv('telecom_churn.csv')  # df는 학습용 데이터
df.dropna(inplace=True)  # 값이 없는 데이터는 전체 삭제해주는 코드

le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])
df['SeniorCitizen'] = le.fit_transform(df['SeniorCitizen'])
df['Partner'] = le.fit_transform(df['Partner'])
df['Dependents'] = le.fit_transform(df['Dependents'])
df['PhoneService'] = le.fit_transform(df['PhoneService'])
df['MultipleLines'] = le.fit_transform(df['MultipleLines'])
df['InternetService'] = le.fit_transform(df['InternetService'])
df['OnlineSecurity'] = le.fit_transform(df['OnlineSecurity'])
df['OnlineBackup'] = le.fit_transform(df['OnlineBackup'])
df['DeviceProtection'] = le.fit_transform(df['DeviceProtection'])
df['TechSupport'] = le.fit_transform(df['TechSupport'])
df['StreamingTV'] = le.fit_transform(df['StreamingTV'])
df['StreamingMovies'] = le.fit_transform(df['StreamingMovies'])
df['Contract'] = le.fit_transform(df['Contract'])
df['PaperlessBilling'] = le.fit_transform(df['PaperlessBilling'])
df['PaymentMethod'] = le.fit_transform(df['PaymentMethod'])
df['Churn'] = le.fit_transform(df['Churn'])

logistic = LogisticRegression(solver='newton-cg')
logistic.fit(df[["gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService", "MultipleLines",
                 "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV",
                 "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod", "MonthlyCharges", "TotalCharges"]],
             df['Churn'])

dd = pd.read_csv('telecom_churn_test.csv')
dd.dropna(inplace=True)

dd['gender'] = le.fit_transform(dd['gender'])
dd['SeniorCitizen'] = le.fit_transform(dd['SeniorCitizen'])
dd['Partner'] = le.fit_transform(dd['Partner'])
dd['Dependents'] = le.fit_transform(dd['Dependents'])
dd['PhoneService'] = le.fit_transform(dd['PhoneService'])
dd['MultipleLines'] = le.fit_transform(dd['MultipleLines'])
dd['InternetService'] = le.fit_transform(dd['InternetService'])
dd['OnlineSecurity'] = le.fit_transform(dd['OnlineSecurity'])
dd['OnlineBackup'] = le.fit_transform(dd['OnlineBackup'])
dd['DeviceProtection'] = le.fit_transform(dd['DeviceProtection'])
dd['TechSupport'] = le.fit_transform(dd['TechSupport'])
dd['StreamingTV'] = le.fit_transform(dd['StreamingTV'])
dd['StreamingMovies'] = le.fit_transform(dd['StreamingMovies'])
dd['Contract'] = le.fit_transform(dd['Contract'])
dd['PaperlessBilling'] = le.fit_transform(dd['PaperlessBilling'])
dd['PaymentMethod'] = le.fit_transform(dd['PaymentMethod'])
dd['Churn'] = le.fit_transform(dd['Churn'])

score = logistic.score(
    dd[["gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService", "MultipleLines",
        "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV",
        "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod", "MonthlyCharges", "TotalCharges"]],
    dd["Churn"])

print(score)