#imports pdf
import pdfminer
print(pdfminer.__version__)  
points = 0
import re
from datetime import datetime

#opens & reads fake-resume.pdf
from io import StringIO
from pdfminer.high_level import extract_text_to_fp
output_string = StringIO()
with open('fakeresume.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string)
print(output_string.getvalue().strip())

from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

pdf_text = extract_text_from_pdf('fakeresume.pdf')

# finds keywords
def find_ed_keywords(text, keywords):
    found_ed_keywords = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_ed_keywords.append(keyword)
    return found_ed_keywords

# keywords to find
ed_keywords_to_search = ['university', 'degree', 'college', 'major', 'minor', 'trade school', 'high school']
ed_found_keywords = find_ed_keywords(pdf_text, ed_keywords_to_search)

# message to say if keywords are found
if ed_found_keywords:
    print("Keywords found:", ed_found_keywords)
else:
    print("No keywords found.")

# rank keywords related to education
def rank_ed(): 
    if 'university' in ed_found_keywords:
        global points
        points += 2
    if 'degree' in ed_found_keywords:
        points += 2
    if 'college' in ed_found_keywords:
        points += 1
    if 'major' in ed_found_keywords:
        points += 1
    if 'minor' in ed_found_keywords:
        points += 1
    if 'trade school' in ed_found_keywords:
        points += 0.5
    if 'major' in ed_found_keywords:
        points += 0.25
rank_ed()

def find_experience_keywords(text, keywords):
    found_exp_keywords = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_exp_keywords.append(keyword)
    return found_exp_keywords

# keywords to find
exp_keywords_to_search = ['']
exp_found_keywords = find_experience_keywords(pdf_text, exp_keywords_to_search)

def rank_exp(): 
    if 'assisted' in exp_found_keywords:
        global points
        points += 0
    if 'Coordinated' in exp_found_keywords:
        points += 2
rank_exp()

if exp_found_keywords:
    print("Experience keywords found:", exp_found_keywords)
else:
    print("No keywords found.")

def extract_dates(pdf_path):
    # Regular expression to find date patterns (e.g., Jan 2010 - Dec 2015)
    date_pattern = r'(\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b \d{4})'
    dates = re.findall(date_pattern, pdf_path)
    return dates

def calculate_experience(dates):
    # Convert date strings to datetime objects
    date_objects = [datetime.strptime(date, '%b %Y') for date in dates]
    
    # Calculate the total experience in years
    total_experience = 0
    for i in range(0, len(date_objects), 2):
        start_date = date_objects[i]
        end_date = date_objects[i + 1] if i + 1 < len(date_objects) else datetime.now()
        total_experience += (end_date - start_date).days / 365.25
    
    return total_experience

# Example resume text
pdf_path = extract_text_from_pdf('fakeresume.pdf')

# Extract dates and calculate experience
dates = extract_dates(pdf_path)
experience_years = calculate_experience(dates)

print(f"Total years of experience: {experience_years:.2f} years")
# prints points Fuck you vincentFuck you vincentFuck you vincentFuck you vincent
print(f'Points: {points}')