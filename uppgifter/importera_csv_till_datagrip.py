import pandas as pd
import psycopg2
 
 
# Anslut till PostgreSQL-databasen
 
conn = psycopg2.connect (
 
    host="localhost",   # Byt ut med din värd
 
    database="postgres",    # Byt ut med din databas
 
    user="postgres",    # Byt ut med ditt användarnamn
 
    password="Hammarby9802",  # Byt ut med ditt lösenord
 
    port="5432"  # Byt ut med din port (oftast 5432 för PostgreSQL
 
)
 
 
cursor = conn.cursor()
 
# Läs in CSV-filen
 
csv_file_path = "/Users/viktorheidmark/Documents/DMSTO24-DS/data_sources/sales_data.csv"  # Sökvägen till din CSV-fil
 
df = pd.read_csv(csv_file_path)
 
# Tabort '****' och ersätt med ditt schema namn rad 37
# Man måste skapa en schema för att kunna skapa en tabell i mitt fall jag skapade schemat 'jag'
 
create_table_query = """
 
    CREATE TABLE IF NOT EXISTS python.sales (          
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
# Tabort '****' och ersätt med ditt schema namn rad 59
 
for index, row in df.iterrows():
 
    insert_query = """
 
    INSERT INTO python.sales (date, product, price, quantity)
    VALUES (%s, %s, %s, %s)
 
"""
 
# Samma sak här jag skapade en ny schema för att kunna lägga till data i tabellen sales den schema kommer innan
# på csv filen alltså jag.sales
 
    cursor.execute(insert_query, (row['Date'], row['Product'], row['Price'], row['Quantity']))
 
# Spara ändringar i databasen
 
conn.commit()
 
# Stäng anslutningen
 
cursor.close()
 
conn.close()
 
print("CSV-filen har importerats till PostgreSQL!")
 
 
 
# För att få detta fungera så måste man skapa en datagrip en databas som heter localhost
# Sedan skapa en schema som heter 'du får välja ett namn' i mitt mitt fall heter min schema 'ds11'
# Sedan man måste ändra i koden på två platser en gång i rad 38 och en gång i rad 59