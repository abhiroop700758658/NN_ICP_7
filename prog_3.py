# Create at least two more visualizations using matplotlib (Other than provided in the source file)
import matplotlib.pyplot as plt import seaborn as sns import pandas as pd
iris _df = pd.DataFrame(data=iris.data, columns=iris.feature _names)
iris_df['target'] = iris.target
sns, pairplot(irs_df, hue= 'target", palettes viridis')
plt. show)
plt. figure(figsize=(10, 6))
sns.boxplot(x='target', y='petal width (cm)', data=iris_df, palette= 'Set3")
plt.xlabel ('Species')
plt.ylabel ('Petal Width (cm)')
plt.title('Distribution of Petal Width across Species')
plt. show)