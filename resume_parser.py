import os
import re
from pdfminer.high_level import extract_text
from database import connect_db

def extract_email(text):
    match = re.search(r'[\w.-]+@[\w.-]+', text)
    return match.group(0) if match else ""

def extract_phone(text):
    match = re.search(r'(\+\d{1,2}\s)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
    return match.group(0) if match else ""

def parse_and_store_resumes(resume_dir):
    conn = connect_db()
    cursor = conn.cursor()

    for filename in os.listdir(resume_dir):
        if filename.endswith(".pdf"):
            path = os.path.join(resume_dir, filename)
            text = extract_text(path)
            email = extract_email(text)
            phone = extract_phone(text)
            cursor.execute("""
                INSERT INTO resumes (filename, name, email, phone, education, experience, skills)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                filename,
                "", email, phone,
                "", "", ""
            ))
    conn.commit()
    conn.close()