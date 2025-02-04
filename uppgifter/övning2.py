
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import psycopg2

csv_file_path = "/Users/viktorheidmark/Documents/DMSTO24-DS/uppgifter/inlämmningsgruppuppgift_2.csv"
df = pd.read_csv(csv_file_path, sep=',')


df.columns = df.columns.str.strip()

#Fyller saknade värden med 0
df.fillna(0, inplace=True)

df.to_excel('/Users/viktorheidmark/Documents/DMSTO24-DS/uppgifter/~$inlämningsgruppuppgift2.xlsx', index=True, sheet_name='inlämningsgruppuppgift_2.xlsx')


#Summera 'amount_sek' per år och kön
df_total = df.groupby(['year', 'gender'], as_index=False).agg({'amount_sek': 'sum'})

#Beräkna procentuell förändring från föregående år
df_total['percent_change'] = df_total.groupby('gender')['amount_sek'].pct_change() * 100


output_csv_path = "/Users/viktorheidmark/Documents/DMSTO24-DS/uppgifter/inlämningsgruppuppgift_2_processeddata.csv"
df_total.to_csv(output_csv_path, index=False)
print(f"Bearbetad data har sparats till {output_csv_path}")

#VISUALISERINGAR 

#Histogram över totalt belopp för arbetslöshetsersättning
plt.figure(figsize=(10, 6))
sns.histplot(df_total['amount_sek'], bins=20, kde=True)
plt.title('Histogram för totalt belopp av arbetslöshetsersättning')
plt.xlabel('Belopp i SEK')
plt.ylabel('Frekvens')
plt.show()

#Linjediagram för att visa trender över tid för varje kön
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_total, x='year', y='amount_sek', hue='gender', marker='o')
plt.title('Linjediagram för arbetslöshetsersättning över tid för varje kön')
plt.xlabel('År')
plt.ylabel('Belopp i SEK')
plt.legend(title='Kön')
plt.show()

#Scatter plot för att visa relationen mellan olika åldersgrupper och belopp
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='age_range_year', y='amount_sek', hue='gender', palette='Set2')
plt.title('Relation mellan åldersgrupper och arbetslöshetsersättning')
plt.xlabel('Åldersgrupp')
plt.ylabel('Belopp i SEK')
plt.legend(title='Kön')
plt.xticks(rotation=45)
plt.show()

#Ny graf: Procentuell förändring över tid
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_total, x='year', y='percent_change', hue='gender', marker='o')
plt.axhline(0, linestyle='--', color='gray')  # Nollinje för att visa när det minskar
plt.title('Procentuell förändring av arbetslöshetsersättning över tid')
plt.xlabel('År')
plt.ylabel('Förändring i %')
plt.legend(title='Kön')
plt.show()

#MASKININLÄRNING: REGRESSION

#Regression för män
df_regression_men = df_total[df_total['gender'] == 'men']
X_men = df_regression_men[['year']]
y_men = df_regression_men['amount_sek']

X_train_men, X_test_men, y_train_men, y_test_men = train_test_split(X_men, y_men, test_size=0.2, random_state=42)

#Träna modellen
model_men = LinearRegression()
model_men.fit(X_train_men, y_train_men)

#Prediktion för män
y_pred_men = model_men.predict(X_test_men)

#Förutsägelse för nästa år (2025) för män
pred_men_2025 = model_men.predict([[2025]])[0]
print(f"Förutsagd arbetslöshetsersättning för män 2025: {pred_men_2025:.2f} SEK")

#Resultatet av regressionen för män
plt.figure(figsize=(10, 6))
plt.scatter(X_test_men, y_test_men, label='Riktiga värden', color='blue')
plt.plot(X_test_men, y_pred_men, label='Prediktion', color='red')
plt.scatter(2025, pred_men_2025, color='green', label='Förutsägelse för 2025', zorder=5)
plt.title('Regression för att förutsäga arbetslöshetsersättning över tid (män)')
plt.xlabel('År')
plt.ylabel('Belopp i SEK')
plt.legend()
plt.show()

#Regression för kvinnor
df_regression_women = df_total[df_total['gender'] == 'women']
X_women = df_regression_women[['year']]
y_women = df_regression_women['amount_sek']

X_train_women, X_test_women, y_train_women, y_test_women = train_test_split(X_women, y_women, test_size=0.2, random_state=42)

#Träna modellen
model_women = LinearRegression()
model_women.fit(X_train_women, y_train_women)

#Prediktion för kvinnor
y_pred_women = model_women.predict(X_test_women)

#Förutsägelse för nästa år (2025) för kvinnor
pred_women_2025 = model_women.predict([[2025]])[0]
print(f"Förutsagd arbetslöshetsersättning för kvinnor 2025: {pred_women_2025:.2f} SEK")

#Resultatet av regressionen för kvinnor
plt.figure(figsize=(10, 6))
plt.scatter(X_test_women, y_test_women, label='Riktiga värden', color='blue')
plt.plot(X_test_women, y_pred_women, label='Prediktion', color='red')
plt.scatter(2025, pred_women_2025, color='green', label='Förutsägelse för 2025', zorder=5)
plt.title('Regression för att förutsäga arbetslöshetsersättning över tid (kvinnor)')
plt.xlabel('År')
plt.ylabel('Belopp i SEK')
plt.legend()
plt.show()


df_total = df.groupby('gender', as_index=False).agg({'amount_sek': 'sum'})

#Skapa regression för förutsägelse för nästa år
df_regression = df_total[['gender', 'amount_sek']]
X = np.array([0, 1]).reshape(-1, 1)  # 0 för män, 1 för kvinnor
y = df_regression['amount_sek'].values
model = LinearRegression().fit(X, y)

#Förutsägelse för 2026
pred_2026 = model.predict([[0], [1]])


#Tårtdiagram för fördelning mellan män och kvinnor
plt.figure(figsize=(6, 6))
sizes = df_total['amount_sek'].values
labels = df_total['gender']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['blue', 'pink'])
plt.title('Fördelning av arbetslöshetsersättning mellan män och kvinnor')
plt.show()

print(f"Förutsägelse för män 2026: {pred_2026[0]:.2f} SEK")
print(f"Förutsägelse för kvinnor 2026: {pred_2026[1]:.2f} SEK")

# Steg 9: Filtrera data för året 2024
df_2024 = df[df['year'] == 2024]

# Kontrollera om 'unemployment_insurance_fund' finns i datasetet
if 'unemployment_insurance_fund' not in df.columns:
    print("'unemployment_insurance_fund' kolumnen saknas i datasetet.")
else:
    # Steg 10: Gruppdata per 'unemployment_insurance_fund' och kön, samt summering av utbetalningar
    grouped_fund_gender = df_2024.groupby(['unemployment_insurance_fund', 'gender'])['amount_sek'].sum().unstack()

    # Steg 11: Visualisering av jämförelse av utbetalningar per 'unemployment_insurance_fund' och kön
    plt.figure(figsize=(14, 7))
    grouped_fund_gender.plot(kind='bar', figsize=(12, 6), cmap='coolwarm', width=0.8)

    plt.title('Jämförelse av utbetalningar per arbetslöshetsförsäkringsfond och kön (2024)', fontsize=16)
    plt.xlabel('Arbetslöshetsförsäkringsfond', fontsize=14)
    plt.ylabel('Totala utbetalningar (SEK)', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Kön', title_fontsize='13')
    plt.tight_layout()
    plt.show()

    # Steg 12: Prediktion för 2025 baserat på 2024 data och antagande om 5% ökning

    # Kontrollera om 'unemployment_insurance_fund' finns i datasetet
    if 'unemployment_insurance_fund' not in df.columns:
        print("'unemployment_insurance_fund' kolumnen saknas i datasetet.")
    else:
        # Gruppdata per 'unemployment_insurance_fund' och kön för 2024
        grouped_fund_gender_2024 = df_2024.groupby(['unemployment_insurance_fund', 'gender'])['amount_sek'].sum().unstack()

        # Beräkna prediktion för 2025 med 5% ökning
        prediction_2025 = grouped_fund_gender_2024 * 1.05

        # Visualisering av prediktion för 2025
        plt.figure(figsize=(14, 7))
        prediction_2025.plot(kind='bar', figsize=(12, 6), cmap='coolwarm', width=0.8, color=['skyblue', 'pink'])

        plt.title('Prediktion av utbetalningar per arbetslöshetsförsäkringsfond och kön (2025)', fontsize=16)
        plt.xlabel('Arbetslöshetsförsäkringsfond', fontsize=14)
        plt.ylabel('Totala utbetalningar (SEK)', fontsize=14)
        plt.xticks(rotation=45, ha='right')
        plt.legend(title='Kön', title_fontsize='13')
        plt.tight_layout()
        plt.show()


# Steg 13: Importera data till PostgreSQL-databasen


# Anslut till PostgreSQL-databasen
conn = psycopg2.connect(
    host="localhost",      # Byt ut med din värd
    database="postgres",   # Byt ut med din databas
    user="postgres",       # Byt ut med ditt användarnamn
    password="Hammarby9802",     # Byt ut med ditt lösenord
    port="5432"            # Byt ut med din port (oftast 5432 för PostgreSQL)
)
 
cursor = conn.cursor()
 
# Skapa schema om det inte finns
# cursor.execute("DROP SCHEMA IF EXISTS 'jag.sales';")
# conn.commit()
cursor.execute("CREATE SCHEMA IF NOT EXISTS jag;")
conn.commit()
 
# Skapa tabellen i schemat 'jag' om den inte finns
create_table_query = """
    CREATE TABLE IF NOT EXISTS jag.sales (          
        unemployment_insurance_fund_id SERIAL PRIMARY KEY,
        year INTEGER,
        unemployment_insurance_fund VARCHAR(50),
        gender VARCHAR(50),
        age_range_year VARCHAR(50),  
        days NUMERIC,
        amount_sek NUMERIC
    );
"""
cursor.execute(create_table_query)
conn.commit()
 
# Läs in CSV-filen
csv_file_path = r"/Users/viktorheidmark/Documents/DMSTO24-DS/uppgifter/inlämmningsgruppuppgift_2.csv"  # Sökvägen till din CSV-fil
df = pd.read_csv(csv_file_path)
 
# Ta bort mellanslag från kolumnnamnen i CSV
df.columns = df.columns.str.strip()
 
# Kontrollera kolumnnamnen i CSV
print("Kolumnnamn i CSV:", df.columns.tolist())
 
# Kontrollera att rätt kolumner finns
expected_columns = ["year", "unemployment_insurance_fund_id", "unemployment_insurance_fund", "gender", "age_range_year", "days", "amount_sek"]
missing_columns = [col for col in expected_columns if col not in df.columns]
 
if missing_columns:
    raise ValueError(f"Följande kolumner saknas i CSV-filen: {missing_columns}")
 
# Iterera genom DataFrame och lägg till data i tabellen
for index, row in df.iterrows():
    # Hantera åldersintervallet korrekt, t.ex. '25-29' -> 25
    age_str = str(row["age_range_year"]).strip()  # Ta bort extra mellanslag
 
    if age_str == "" or age_str.lower() == "nan":
        age_value = None  # Eller sätt 0 om du vill ha ett numeriskt standardvärde
    elif "-" or "+" in age_str:
        age_value = str(age_str)
    #     try:
    #         age_value = str(age_str.split("-")[1])
    #         print(age_str.split("-"))
    #         # age_value = str(age_str.split("+")[0])
    #     except ValueError:
    #         print(f"⚠️ Ogiltigt värde för åldersintervall i rad {index}: {age_str}. Sätt åldern till None.")
    #         age_value = None
    # elif "+" in age_str:
    #     try:
    #         print(age_value)
    #     except ValueError:
    #         print(f"⚠️ Ogiltigt värde för åldersintervall i rad {index}: {age_str}. Sätt åldern till None.")
    #         age_value = None
    else:
        try:
            age_value = int(age_str)
        except ValueError:
            print(f"⚠️ Ogiltigt värde för ålder i rad {index}: {age_str}. Sätt åldern till None.")
            age_value = None
 
    # Hantera felaktiga eller tomma värden för 'days' och 'amount_sek'
    try:
        days = float(row["days"]) if row["days"] != "" else None
    except ValueError:
        days = None
 
    try:
        amount_sek = float(row["amount_sek"]) if row["amount_sek"] != "" else None
    except ValueError:
        amount_sek = None
 
    # Försök att införa rad i tabellen
    insert_query = """
        INSERT INTO jag.sales (year, unemployment_insurance_fund, gender, age_range_year, days, amount_sek)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (row["year"], row["unemployment_insurance_fund"], row["gender"], str(age_value), days, amount_sek))
 
# Spara ändringar
conn.commit()
 
# Stäng anslutningen
cursor.close()
conn.close()
 
print(" CSV-filen har importerats till PostgreSQL!")
 
