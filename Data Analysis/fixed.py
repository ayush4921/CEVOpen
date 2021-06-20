import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('Plant_compound.csv')
df_transposed = df.set_index('PlantName').copy().transpose()
plt.figure(figsize=(20, 23))
sns.heatmap(df_transposed.corr(), annot=True, linewidth=0.5, cmap='coolwarm')
plt.show()
