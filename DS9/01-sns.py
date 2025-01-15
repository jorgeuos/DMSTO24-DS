"""
Installera först seaborn:
$ pip install seaborn
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {"Category": ["A", "B", "C"], "Values": [10, 20, 15]}
df = pd.DataFrame(data)

sns.barplot(x="Category", y="Values", data=df)

plt.show()

