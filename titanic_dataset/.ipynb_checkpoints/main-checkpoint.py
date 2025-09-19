import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# read the data
df = pd.read_csv('train.csv')

# Cleaning Data
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Cabin'] = df['Cabin'].fillna('unknown')
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# bins & label for cut
bins = [0, 10, 20, 30, 40, 50, 60,  70, 80]
labels = ["0-10", "10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80"]

# make aggregate data
d_agg = df.copy()
d_agg["Age"] = pd.cut(df['Age'],bins=bins, labels=labels, right=True)
d_agg.drop(columns="Name", inplace=True)

# aggreate data by something
d_agg_survived_age = d_agg.groupby("Age", as_index=False)['Survived'].agg([
    ('survived_count', 'count'),
    ('Survived', 'sum')
])

d_agg_survived_sex = d_agg.groupby("Sex", as_index=False)['Survived'].agg([
    ('survived_count', 'count'),
    ('Survived', 'sum')
])

d_agg_survived_pclass = d_agg.groupby("Pclass", as_index=False)['Survived'].agg([
    ('survived_count', 'count'),
    ('Survived', 'sum')
])


# count the precentage of surviving
d_agg_survived_age["Survival_rate"] = (d_agg_survived_age["Survived"] / d_agg_survived_age["survived_count"]) * 100
d_agg_survived_sex["Survival_rate"] = (d_agg_survived_sex["Survived"] / d_agg_survived_sex["survived_count"]) * 100
d_agg_survived_pclass["Survival_rate"] = (d_agg_survived_pclass["Survived"] / d_agg_survived_pclass["survived_count"]) * 100


# Data visualitazion
def data_visualitazion(data, x, y, kind):
    data.plot(x=x, y=y, kind=kind)
   
data_visualitazion(d_agg_survived_age, "Age", "Survival_rate", "bar")
data_visualitazion(d_agg_survived_sex, "Sex", "Survival_rate", "bar")
data_visualitazion(d_agg_survived_pclass, "Pclass", "Survival_rate", "bar")

plt.show()