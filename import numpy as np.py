import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('/Users/ilyasserraji/desktop/titanic3.csv',delimiter=';')
print(data.shape)
print(data.describe)
data = data.drop(['name', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'], axis=1)
data = data.dropna(axis=0)
print(data.shape)
data['age'] = data['age'].str.replace(',', '').astype(int)
print(data.groupby(['sex', 'pclass']).mean())
print(data['pclass'].value_counts())
print(data[data['age'] < 18]['pclass'].value_counts())
print(data[data['age'] < 18].groupby(['sex', 'pclass']).mean())
def cat_age(age):
    if age <= 20:
        return '<20 ans'
    elif (age > 20) & (age <= 30):
        return '20-30 ans'
    elif (age > 30) & (age <= 40):
        return '30-40 ans'
    else:
        return '+40 ans'
data['age']=(data['age'].map(cat_age))
print(data['age'].value_counts())
