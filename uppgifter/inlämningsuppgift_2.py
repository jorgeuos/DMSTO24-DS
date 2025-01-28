#inlämnings uppgift 2
#fördelning av arbetslöshet mellan kvinnor och män


# Importera pandas för filhantering och dataanalys, matplotlib för att skapa diagram och seaborn för att förbättra diagrammen.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Hämta ett dataset från dataportal.se. Exempel: befolkningsstatistik, trafikdata,
# energiförbrukning.
# Importera datan till Python med hjälp av pandas.read csv() eller motsvarande metod.
url = 'https://catalog.iaf.se/store/1/resource/186'
df = pd.read_csv(url)

# visa de första 5 raderna i dataframen
print(df.head())

# sparar dataframen till en csv fil
df.to_csv('/Users/viktorheidmark/Documents/DMSTO24-DS/uppgifter/inlämningsuppgift_2.csv', index=False)

#spara dataframen till en csv fil och skriver ut det i terminalen
print("Data sparad i inlämningsuppgift_2.csv")

# laddar ned data
df = pd.read_csv('/Users/viktorheidmark/Documents/DMSTO24-DS/uppgifter/inlämningsuppgift_2.csv')

# visar de första 5 raderna i dataframen
print(df.head())

# Hantera saknade värden.
df.fillna(0, inplace=True)

# Skapa nya kolumner baserat på beräkningar eller villkor
df['total'] = df['women'] + df['men']
df['women_percentage'] = round((df['women'] / df['total']) * 100, 1)
df['men_percentage'] = round((df['men'] / df['total']) * 100, 1)

df.to_csv('/Users/viktorheidmark/Documents/DMSTO24-DS/uppgifter/inlämningsuppgift_2.csv', index=False)


# Filtrera datan för att fokusera på relevanta insikter.
filtered_df = df[df['total'] > 600000]

# visar den filtrerade datan
print(filtered_df)


# ■ Använd groupby() och agg() för att summera och analysera nyckeltal.
summary = filtered_df.groupby('year').agg({
    'women': 'sum',
    'men': 'sum',
    'total': 'sum',
    'women_percentage': 'mean',
    'men_percentage': 'mean'
})

# visar en summering av dataframen
print(summary)


# Exportera den bearbetade datan till en Excel-fil med to excel().
summary.to_excel('/Users/viktorheidmark/Documents/DMSTO24-DS/uppgifter/processed_data.xlsx', index=True, sheet_name='processed_data.xlsx')

print("Processed data has been saved to processed_data.xlsx")


# Histogram för datafördelning för att visa hur datan är fördelad.
plt.figure(figsize=(10, 6))
sns.histplot(df['total'], bins=20, kde=True)
plt.title('Histogram för datafördelning')
plt.xlabel('Total befolkning')
plt.ylabel('Frekvens')
plt.show()

# Linjediagram för att visa trender över tid.
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='year', y='total', label='Total')
sns.lineplot(data=df, x='year', y='women', label='Women')
sns.lineplot(data=df, x='year', y='men', label='Men')
plt.title('Linjediagram för att visa trender över tid')
plt.xlabel('År')
plt.ylabel('Befolkning')
plt.legend()
plt.show()


# Scatter plot för att visa relationer mellan två variabler med årtal på varje punkt.
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='women', y='men')
plt.title('Scatter plot för att visa relationer mellan två variabler.')
plt.xlabel('Kvinnor befolkning')
plt.ylabel('Män befolkning')
plt.grid(True, color= 'black', linestyle='--', linewidth=0.5)

# Lägg till årtal på varje punkt
for i in range(0, df.shape[0]):
    plt.text(df.women[i], df.men[i], df.year[i], horizontalalignment='left', size='medium', color='black', weight='semibold')

plt.show()


print("Histogram visar hur datan är fördelad.")
print("Linjediagram visar trender över tid")
print("Scatter plot visar relationer mellan två variabler med årtal på varje punkt")