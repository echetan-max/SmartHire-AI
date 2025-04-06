from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from database import connect_db

def calculate_and_store_matches():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM job_descriptions")
    jds = cur.fetchall()

    cur.execute("SELECT * FROM resumes")
    cvs = cur.fetchall()

    for jd in jds:
        jd_id = jd[0]
        jd_text = " ".join(map(str, jd[1:]))
        for cv in cvs:
            cv_id = cv[0]
            cv_text = " ".join(map(str, cv[2:]))
            texts = [jd_text, cv_text]
            vec = TfidfVectorizer().fit_transform(texts)
            score = cosine_similarity(vec[0:1], vec[1:2])[0][0] * 100
            cur.execute("""
                INSERT INTO match_results (job_id, resume_id, score)
                VALUES (?, ?, ?)
            """, (jd_id, cv_id, score))
    conn.commit()
    conn.close()