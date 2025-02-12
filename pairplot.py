import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = "Sample_Data_for_Activity.csv"  # Update this with the correct path
df = pd.read_csv(file_path)

# Generate the pair plot
sns.pairplot(df)
plt.show()
