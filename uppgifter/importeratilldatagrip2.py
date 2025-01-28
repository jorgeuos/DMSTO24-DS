import pandas as pd
import psycopg2

# Anslut till PostgreSQL-databasen
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Hammarby9802",
    port="5432"
)
cursor = conn.cursor()

try:
    # Skapa tabellen i PostgreSQL om den inte redan finns
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
    print("Tabellen 'sales' har skapats i PostgreSQL!")
except Exception as e:
    print("Databas finns redan")


# Relativ sökväg, relativ till där filen som exekveras ligger i
csv_file_path = "/Users/viktorheidmark/Documents/DMSTO24-DS/DS9/ovningar/customers.csv"  # Sökvägen till din CSV-fil
df = pd.read_csv(csv_file_path)

print(df.head())

# Iterera genom DataFrame och lägg till data i tabellen
for index, row in df.iterrows():
    insert_query = """
    INSERT INTO python.sales (date, product, price, quantity)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (row['Date'], row['Product'], row['Price'], row['Quantity']))

# Spara ändringar i databasen
conn.commit()

# Stäng anslutningen
cursor.close()
conn.close()

print("CSV-filen har importerats till PostgreSQL!")



