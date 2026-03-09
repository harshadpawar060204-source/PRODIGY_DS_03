import pandas as pd
url = "https://raw.githubusercontent.com/Prodigy-InfoTech/data-science-datasets/main/Task%203/bank-additional/bank-additional-full.csv"
data = pd.read_csv(url, sep=';')
print("Dataset shape:", data.shape)
print("Columns:", data.columns)
print(data.head())
print(data.isnull().sum())
data_encoded = pd.get_dummies(data, drop_first=True)
import matplotlib.pyplot as plt
import seaborn as sns

# Target distribution
sns.countplot(x='y', data=data)
plt.title("Subscription Distribution")
plt.show()

# Age distribution
sns.histplot(data['age'], bins=20, kde=True)
plt.title("Age Distribution of Clients")
plt.show()

# Subscription by job
sns.countplot(x='job', hue='y', data=data)
plt.xticks(rotation=45)
plt.title("Subscription by Job Type")
plt.show()

# Subscription by education
sns.countplot(x='education', hue='y', data=data)
plt.xticks(rotation=45)
plt.title("Subscription by Education Level")
plt.show()