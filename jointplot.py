import seaborn as sns
import matplotlib.pyplot as plt

sns.jointplot(data=df, x="column_x", y="column_y", kind="scatter")
plt.show()
