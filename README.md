# SmartHire AI: Multi-Agent System for Intelligent Talent Screening

SmartHire AI is a complete multi-agent system that streamlines the recruitment process by parsing resumes, summarizing job descriptions, matching candidates with at least 80% relevance, shortlisting them, and sending out personalized interview invitations. All data is stored and managed using SQLite.

##  Features

-  Multi-Agent Architecture
  - JD Summarizer
  - CV Parser
  - Candidate Matcher
  - Shortlisting Agent
  - Email Scheduler
  - SQLite Storage Manager

-  Resume Parsing** from PDFs
-  80%+ Match Threshold** for candidate selection
-  Email Invitations** generated in the `emails/` folder
-  Persistent Storage** using `smarthire.db`
-  Outputs: `shortlisted.csv`, database records, and emails


## Folder Structure

SmartHire_AI/
├── agents/
│   ├── jd_summarizer.py
│   ├── resume_parser.py
│   ├── matcher.py
│   ├── shortlister.py
│   ├── scheduler.py
│   └── storage.py
├── resumes/               # Input: 200 candidate resumes (PDF)
├── job_description.csv    # Input: Job Description file
├── shortlisted.csv        # Output: Final shortlisted candidates
├── emails/                # Output: Interview invitation emails
├── smarthire.db           # SQLite database file
├── run.py                 # Main runner script
└── README.md

## Setup Instructions

1. Install Dependencies
   
   pip install -r requirements.txt
  
2. Add Input Files
   - Place your resumes in the `resumes/` folder (PDF format).
   - Ensure your `job_description.csv` is in the root directory.


## How to Run


python run.py


This will:
- Summarize the job description
- Parse all resumes
- Match candidates based on 80%+ similarity
- Store data in SQLite (`smarthire.db`)
- Output the shortlisted candidates in `shortlisted.csv`
- Generate invitation emails in the `emails/` directory



##Tech Stack

- Python 3.8+
- SQLite
- pandas, sklearn, PyPDF2

