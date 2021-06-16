# Creación de un modelo completo
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNetCV as eNetCv
from sklearn import metrics

def build_modelo(X_train, y_train):
   model_math = eNetCv(alphas=np.linspace(0.001, 10, 100), cv = 3, n_jobs=8, verbose=0)
   model_math.fit(X_train, y_train['math_score'])
   return model_math
# en model_math me queda el modelo entrenado para predecir el resultado en matemática

def score_modelo(y_test, y_pred ):
    return metrics.r2_score(y_test, y_pred)

def implemento_modelo(elCSV):
    df = pd.read_csv(elCSV)
  # reemplazamos los espacios por _ 
    df.columns = [x.replace(' ', '_') for x in df.columns]

    columnas_categoricas = ['gender', 'race/ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
    columnas_respuestas  = ['math_score', 'reading_score', 'writing_score']

    df_dummies = pd.get_dummies(df, columns = columnas_categoricas)
    df_dummies.sample(4)

    X = df_dummies.drop(labels = columnas_respuestas, axis=1)
    y = df_dummies[[x for x in df_dummies.columns if x in columnas_respuestas]]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

    modelo = build_modelo(X_train, y_train)
    y_pred = modelo.predict(X_test)

    return(score_modelo(y_test.math_score, y_pred))