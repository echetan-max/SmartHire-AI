def generate_email(name, score):
    return f"""Hi {name},

Congratulations! Based on your resume, you've been shortlisted with a match score of {score:.2f}%.
We would like to invite you to an interview. Please choose a convenient time from the following:

- Date: [Insert Date]
- Time Slots: 10:00 AM, 2:00 PM, 4:00 PM
- Format: Online (Zoom)

Best,
HR Team
"""