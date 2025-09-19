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
bins_age = [0, 10, 20, 30, 40, 50, 60, 70, 80]
labels_age = ["0-10", "10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80"]

bins_family = [0, 1, 3, 20]
labels_family = ["Single", "Small", "Large"]


df["Age_group"] = pd.cut(df['Age'], bins=bins_age, labels=labels_age, right=True)
df["Family_Category"] = pd.cut(df['SibSp'] + df['Parch'] + 1, bins=bins_family, labels=labels_family, right=True)
# === 5. Aggregate Survival Data ===

# by Age Group
survived_by_age = df.groupby("Age_group", observed=False).agg(
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

# by family size
survived_by_familysize = df.groupby("Family_Category", observed=False).agg(
    survived_count=("Survived", "count"),
    survived_sum=("Survived", "sum")
).reset_index()
survived_by_familysize["Survival_rate"] = (
    survived_by_familysize["survived_sum"] / survived_by_familysize["survived_count"] * 100
)

# === 6. Visualization ===

fig, axes = plt.subplots(2, 2, figsize=(18, 6))

# Survival by Age Group
sns.barplot(data=survived_by_age, x="Age_group", y="Survival_rate", ax=axes[0, 0])
axes[0, 0].set_title("Survival Rate by Age Group")
axes[0, 0].set_ylabel("Survival Rate (%)")

# Survival by Sex
sns.barplot(data=survived_by_sex, x="Sex", y="Survival_rate", ax=axes[0, 1])
axes[0, 1].set_title("Survival Rate by Sex")
axes[0, 1].set_ylabel("Survival Rate (%)")

# Survival by Pclass
sns.barplot(data=survived_by_pclass, x="Pclass", y="Survival_rate", ax=axes[1, 0])
axes[1, 0].set_title("Survival Rate by Passenger Class")
axes[1, 0].set_ylabel("Survival Rate (%)")

sns.barplot(data=survived_by_familysize, x="Family_Category", y="Survival_rate", ax=axes[1, 1])
axes[1, 1].set_title("Survival Rate by Family Size")
axes[1, 1].set_ylabel("Survival Rate (%)")

plt.tight_layout()
plt.show()