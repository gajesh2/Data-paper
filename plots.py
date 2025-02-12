import pandas as pd
dfile_path = "Sample_Data_for_Activity.csv"
df = pd.read_csv(dfile_path)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("whitegrid")
sns.displot(df["Normal_Distribution"], kde=True, bins=30)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Distribution Plot of Normal_Distribution")
plt.show()
