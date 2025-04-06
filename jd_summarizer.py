import pandas as pd
from database import connect_db

def summarize_and_store_jds(filepath):
    df = pd.read_csv(filepath, encoding='ISO-8859-1')
    conn = connect_db()
    cursor = conn.cursor()
    
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO job_descriptions (title, description, responsibilities, qualifications, skills)
            VALUES (?, ?, ?, ?, ?)
        """, (
            row.get("Title", ""),
            row.get("Description", ""),
            row.get("Responsibilities", ""),
            row.get("Qualifications", ""),
            row.get("Skills", "")
        ))
    conn.commit()
    conn.close()