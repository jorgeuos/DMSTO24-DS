import pandas as pd
import psycopg2

# Anslut till PostgreSQL-databasen
conn = psycopg2.connect(
    host="localhost",  # Byt ut med din värd
    database="din_databas",  # Byt ut med din databas
    user="ditt_användarnamn",  # Byt ut med ditt användarnamn
    password="ditt_lösenord"  # Byt ut med ditt lösenord
)
cursor = conn.cursor()

# Läs in CSV-filen
csv_file_path = "sales_data.csv"  # Sökvägen till din CSV-fil
df = pd.read_csv(csv_file_path)

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

# Iterera genom DataFrame och lägg till data i tabellen
for index, row in df.iterrows():
    insert_query = """
    INSERT INTO sales (date, product, price, quantity, sales)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (row['Date'], row['Product'], row['Price'], row['Quantity'], row['Sales']))

# Spara ändringar i databasen
conn.commit()

# Stäng anslutningen
cursor.close()
conn.close()

print("CSV-filen har importerats till PostgreSQL!")



