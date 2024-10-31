import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns

madan_data = pd.read_csv("./dataset/Madan_pRecall_database.csv")

# 1. Descriptive Statistics and Data Exploration:

# Examine the data structure and summary statistics
print(madan_data.info())  # data types and missing infos
print(madan_data.describe())

# Create frequency bins based on WFlog
madan_data['freq_bin'] = pd.qcut(madan_data['WFlog'], 3, labels=["Low", "Medium", "High"])

# Visualize distributions of key variables
plt.figure(figsize=(10, 6))
sns.histplot(madan_data['pRecall'], bins=20, kde=True, color='blue')
plt.xlabel("Recall Probability")
plt.ylabel("Frequency")
plt.title("Distribution of Recall Probabilities")
plt.show()

# Visualize distributions of other key variables
plt.figure(figsize=(10, 6))
sns.histplot(madan_data['Concreteness'].dropna(), bins=20, kde=True, color='green')
plt.xlabel("Concreteness")
plt.ylabel("Frequency")
plt.title("Distribution of Concreteness")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(madan_data['Arousal'], bins=20, kde=True, color='red')
plt.xlabel("Arousal")
plt.ylabel("Frequency")
plt.title("Distribution of Arousal")
plt.show()

# Create box plots to explore distributions
plt.figure(figsize=(10, 6))
sns.boxplot(x='freq_bin', y='pRecall', data=madan_data)
plt.xlabel("Frequency Bin")
plt.ylabel("Recall Probability")
plt.title("Box Plot of Recall Probability by Frequency Bin")
plt.show()

# Create violin plots to explore distributions
plt.figure(figsize=(10, 6))
sns.violinplot(x='freq_bin', y='pRecall', data=madan_data)
plt.xlabel("Frequency Bin")
plt.ylabel("Recall Probability")
plt.title("Violin Plot of Recall Probability by Frequency Bin")
plt.show()

# Create scatter plots to explore relationships between variables
sns.pairplot(madan_data[['pRecall', 'nLet', 'WFlog', 'Animacy', 'Concreteness', 'Valence', 'Arousal']], diag_kind='kde')
plt.show()



# 2. Replicating Key Findings:

# a) Correlation between recall probability and word properties:
correlations = madan_data[['pRecall', 'nLet', 'nSyl', 'WFlog', 'Animacy', 'Concreteness', 'Valence', 'Arousal']].corr(method='spearman')
print(correlations)

# Visualize correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlations, annot=True, cmap='coolwarm', center=0)
plt.title("Correlation Matrix")
plt.show()

# b) Linear Regression (example with nLet and WFlog):
model = smf.ols('pRecall ~ nLet + WFlog', data=madan_data).fit()
print(model.summary())

# Additional regression with more variables
model2 = smf.ols('pRecall ~ nLet + WFlog + Concreteness + Arousal', data=madan_data).fit()
print(model2.summary())

# 3. Extending the Analysis (Examples):

# a) Impact of Word Length on Memorability Across Frequency Bands:
for bin in madan_data['freq_bin'].unique():
    bin_data = madan_data[madan_data['freq_bin'] == bin]
    correlation = stats.spearmanr(bin_data['pRecall'], bin_data['nLet'])
    print(f"Correlation in {bin} Frequency Bin: {correlation}")

# Visualize the impact of word length on memorability across frequency bands
plt.figure(figsize=(10, 6))
sns.boxplot(x='freq_bin', y='nLet', data=madan_data)
plt.xlabel("Frequency Bin")
plt.ylabel("Number of Letters")
plt.title("Box Plot of Number of Letters by Frequency Bin")
plt.show()

# b) Exploring Animacy and Usefulness Interactions:
interaction_model = smf.ols('pRecall ~ Animacy * Usefulness', data=madan_data.dropna(subset=['Animacy', 'Usefulness'])).fit()
print(interaction_model.summary())

# Visualize interaction effects
plt.figure(figsize=(10, 6))
sns.lmplot(x='Animacy', y='pRecall', hue='Usefulness', data=madan_data.dropna(subset=['Animacy', 'Usefulness']), aspect=1.5)
plt.xlabel("Animacy")
plt.ylabel("Recall Probability")
plt.title("Interaction Effect of Animacy and Usefulness on Recall Probability")
plt.show()
