import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://catalog.ale.se/store/1/resource/65"
df = pd.read_csv(url)

print(df.head())

df.to_csv("/Users/viktorheidmark/Documents/DMSTO24-DS/ovningar/analys_____2.csv")

print("Data sparad i analys_____2.csv")