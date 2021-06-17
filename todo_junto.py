import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNetCV as eNetCv
from sklearn import metrics

print('Suma 21+5: ', 21+5)
print('Resta: 26-5: ', 26 - 5)

print('Suma 10+4 : ', 10+4)
print('Resta: 126-45: ', 126 - 45)

df = pd.read_csv('StudentsPerformance.csv')
 # reemplazamos los espacios por _ 
df.columns = [x.replace(' ', '_') for x in df.columns]

columnas_categoricas = ['gender', 'race/ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
columnas_respuestas  = ['math_score', 'reading_score', 'writing_score']

df_dummies = pd.get_dummies(df, columns = columnas_categoricas)
df_dummies.sample(4)

X = df_dummies.drop(labels = columnas_respuestas, axis=1)
y = df_dummies[[x for x in df_dummies.columns if x in columnas_respuestas]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

model_math = eNetCv(alphas=np.linspace(0.001, 10, 100), cv = 3, n_jobs=8, verbose=0)
model_math.fit(X_train, y_train['math_score'])

y_pred = model_math.predict(X_test)

r2 = metrics.r2_score(y_test.math_score, y_pred)

print('R2: ', r2)