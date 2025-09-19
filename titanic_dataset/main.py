# === 1. Import Library ===
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Style seaborn biar lebih enak dilihat
sns.set_theme(style="whitegrid", palette="muted")

# === 2. Load Dataset ===
df = pd.read_csv("train.csv")
df.head()

# === 3. Data Cleaning ===
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Cabin'] = df['Cabin'].fillna('Unknown')
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# === 4. Feature Engineering: Binning Age ===
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
labels = ["0-10", "10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80"]

df["AgeGroup"] = pd.cut(df['Age'], bins=bins, labels=labels, right=True)

# === 5. Aggregate Survival Data ===

# by Age Group
survived_by_age = df.groupby("AgeGroup", observed=False).agg(
    survived_count=("Survived", "count"),
    survived_sum=("Survived", "sum")
).reset_index()
survived_by_age["Survival_rate"] = survived_by_age["survived_sum"] / survived_by_age["survived_count"] * 100

# by Sex
survived_by_sex = df.groupby("Sex", observed=False).agg(
    survived_count=("Survived", "count"),
    survived_sum=("Survived", "sum")
).reset_index()
survived_by_sex["Survival_rate"] = survived_by_sex["survived_sum"] / survived_by_sex["survived_count"] * 100

# by Pclass
survived_by_pclass = df.groupby("Pclass", observed=False).agg(
    survived_count=("Survived", "count"),
    survived_sum=("Survived", "sum")
).reset_index()
survived_by_pclass["Survival_rate"] = survived_by_pclass["survived_sum"] / survived_by_pclass["survived_count"] * 100

# === 6. Visualization ===

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Survival by Age Group
sns.barplot(data=survived_by_age, x="AgeGroup", y="Survival_rate", ax=axes[0])
axes[0].set_title("Survival Rate by Age Group")
axes[0].set_ylabel("Survival Rate (%)")

# Survival by Sex
sns.barplot(data=survived_by_sex, x="Sex", y="Survival_rate", ax=axes[1])
axes[1].set_title("Survival Rate by Sex")
axes[1].set_ylabel("Survival Rate (%)")

# Survival by Pclass
sns.barplot(data=survived_by_pclass, x="Pclass", y="Survival_rate", ax=axes[2])
axes[2].set_title("Survival Rate by Passenger Class")
axes[2].set_ylabel("Survival Rate (%)")

plt.tight_layout()
plt.show()