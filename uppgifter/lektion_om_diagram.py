import seaborn as sns
import matplotlib.pyplot as plt
 
 
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]
 
#histogram,  #kde är kurva  #bins är antal staplar
sns.histplot(data, bins=7, kde=True)
 
#titel
plt.title('Enkel histogram')
 
 
plt.show()