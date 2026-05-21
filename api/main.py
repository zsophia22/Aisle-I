"""
POST /receipts/upload
GET /pantry
GET /pantry/expiring
POST /meal-plans/generate
GET /meal-plans/{id}
"""

from fastapi import FASTAPI 
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel 
from db.create_tables import connect_db
import json

app = FASTAPI() 

@app.get("/pantry")
def get_pantry():
    #connect to postgres db
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
            SELECT * from pantry_items
            WHERE quantity > 0;
                   """)
    rows = cursor.fetchall()
    json_output = json.dumps(rows, indent=4, default=str)
    #print(json_output)

    #close connection to db
    cursor.close()
    conn.close()

    return jsonable_encoder(rows)

@app.get("/")
def get_expiring():
    return {}

@app.post("/receipts/upload/{filepath}")
def upload_receipts(filepath: str):
    
    return {}

@app.post("/")
def generate_meal_plans():
    return {}
