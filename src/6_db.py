import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="aisle-i-db",
    user="sophiazheng",
    password=""
)

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS receipts (
               id SERIAL PRIMARY KEY, 
               filepath VARCHAR(500) NOT NULL, 
               date DATE NOT NULL, 
               processed BOOLEAN DEFAULT FALSE, 
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
               """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS ingredients (
               id SERIAL PRIMARY KEY, 
               name TEXT NOT NULL, 
               category VARCHAR(100))
               """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS pantry_items (
               id SERIAL PRIMARY KEY, 
               ingredient_id INTEGER REFERENCES ingredients(id),
               quantity NUMERIC, 
               unit VARCHAR(50), 
               expiration_date DATE,
               receipt_id INTEGER REFERENCES receipts(id),
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
               """)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS recipes (
               id SERIAL PRIMARY KEY, 
               title TEXT NOT NULL, 
               cuisine_type VARCHAR(100) ,
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
               """)

#create a table that can answer "What recipes can I make with what's in pantry"
#recipe name lives in recipe and ingredient name lives in pantry_item
cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipe_ingredients (
               id SERIAL PRIMARY KEY, 
               recipe_id INTEGER REFERENCES recipes(id),
               ingredient_id INTEGER REFERENCES ingredients(id),
               quantity NUMERIC, 
               unit VARCHAR(50))
               """)



conn.commit()
cursor.close()
conn.close()
print("tables created!")