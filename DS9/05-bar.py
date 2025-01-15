import matplotlib.pyplot as plt
import seaborn as sns

categories = ["A", "B", "C"]
values = [10, 20, 15]

sns.set_theme(style="ticks")
sns.set_palette("muted")


sns.barplot(x="Category", y="Values", data={"Category": categories, "Values": values})
# plt.bar(categories, values, color=["blue", "green", "orange"])

plt.title("Anpassat stapeldiagram")
plt.show()
