import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataset= pd.read_csv('data.csv',sep=';')
print("Ukuran dataset:", dataset.shape)
print (dataset.head(10))
dataset_feature = dataset['ProcessedText'].astype(str)
dataset_label = dataset['Sentimen']
print (dataset_feature.head(10))
print (dataset_label.head(10))
plt.figure(figsize=(12,8))
sns.histplot(dataset_label,kde=True, label=f'target, skew: {dataset_label.skew():.2f}')
plt.legend(loc='best')
plt.show()

print (dataset_label.value_counts())