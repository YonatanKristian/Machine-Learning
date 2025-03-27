import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset
dataset=pd.read_csv("data.csv",sep=';')


# Tampilkan ukuran dataset
print("Ukuran dataset:", dataset.shape)

# Konversi kolom ke string
dataset_feature = dataset['ProcessedText'].astype(str)
dataset_label = dataset['Sentimen']

plt.figure(figsize=(12,8))
sns.histplot(dataset_label,kde=True, label=f'target, skew: {dataset_label.skew():.2f}')
plt.legend(loc='best')
plt.show()


# Menampilkan jumlah masing-masing label sentimen
print("Jumlah data tiap sentimen:\n", dataset_label.value_counts())

