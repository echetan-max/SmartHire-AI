from database import connect_db

def shortlist_candidates(threshold=80):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT r.filename, m.score FROM match_results m
        JOIN resumes r ON m.resume_id = r.id
        WHERE m.score >= ?
    """, (threshold,))
    results = cur.fetchall()
    conn.close()
    return results