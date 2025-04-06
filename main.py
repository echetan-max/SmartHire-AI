from database import create_tables
from jd_summarizer import summarize_and_store_jds
from resume_parser import parse_and_store_resumes
from match_engine import calculate_and_store_matches
from shortlist import shortlist_candidates
from scheduler import generate_email

def run_pipeline():
    create_tables()
    summarize_and_store_jds("job_description.csv")
    parse_and_store_resumes("resumes")
    calculate_and_store_matches()
    shortlisted = shortlist_candidates()

    for filename, score in shortlisted:
        name = filename.split(".")[0]
        email = generate_email(name, score)
        print(f"--- Interview Email for {name} ---")
        print(email)
        print("----------------------------------\n")

if __name__ == "__main__":
    run_pipeline()