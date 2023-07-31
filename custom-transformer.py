import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

# TODO: Modify this list to include the numerical columns

df = pd.read_csv('raw-data.csv')
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
NUMERICAL_VARS = data.select_dtypes(include=numerics).columns

# Crear custom transformer


class MissingIndicator(BaseEstimator, TransformerMixin):

    def __init__(self, variables):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y):
        return self

    def transform(self, X):
        # TODO: Put your code here
        for i in NUMERICAL_VARS:
            print(i+'_nan',df[i].isnull().tolist())
            df[i+'_nan']=list(map(int,df[i].isnull().tolist()))
        return X


# Leer el csv sin aplicar transformaciones
df = pd.read_csv("raw-data.csv")

# Imprimir los primeros datos
print(df.head(10))

mi = MissingIndicator(variables=NUMERICAL_VARS)
# Aplicar las transformaciones
df_mi = mi.transform(df)

# Imprimir resultados despues de las transformaciones
print(df_mi.head(20))