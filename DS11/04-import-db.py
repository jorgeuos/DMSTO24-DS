import pandas as pd
import psycopg2

# Anslut till PostgreSQL-databasen
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres",
    port=5433
)
cursor = conn.cursor()

try:
    # Skapa tabellen i PostgreSQL om den inte redan finns
    create_table_query = """
    CREATE TABLE IF NOT EXISTS sales (
        id SERIAL PRIMARY KEY,
        date DATE,
        product VARCHAR(50),
        price NUMERIC,
        quantity INTEGER,
        sales NUMERIC
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    print("Tabellen 'sales' har skapats i PostgreSQL!")
except Exception as e:
    print("Databas finns redan")

# Läs in CSV-filen

# Sökväg relativ till där filen exekveras ifrån
# csv_file_path = "sales_data.csv"  # Sökvägen till din CSV-fil

# Absolut sökväg
# Windows
# csv_file_path = "C:\sökväg\till\din\CSV-fil.csv"  # Sökvägen till din CSV-fil
# På MIN Mac
# /Users/jorge/projects/tuc/DataScience/data_sources/sales_data.csv
# I VSCode kan man kopiera absolut sökväg genom att högerklicka på filen och välja "Copy Path"

# Relativ sökväg, relativ till där filen som exekveras ligger i
csv_file_path = "../data_sources/sales_data.csv"  # Sökvägen till din CSV-fil
df = pd.read_csv(csv_file_path)

print(df.head())

# Iterera genom DataFrame och lägg till data i tabellen
for index, row in df.iterrows():
    insert_query = """
    INSERT INTO sales (date, product, price, quantity)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (row['Date'], row['Product'], row['Price'], row['Quantity']))

# Spara ändringar i databasen
conn.commit()

# Stäng anslutningen
cursor.close()
conn.close()

print("CSV-filen har importerats till PostgreSQL!")



