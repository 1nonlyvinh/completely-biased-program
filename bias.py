#imports pdf
import pdfminer
print(pdfminer.__version__)  
points = 0
import re
years = re.findall(r'\d+', text)

#opens & reads fake-resume.pdf
from io import StringIO
from pdfminer.high_level import extract_text_to_fp
output_string = StringIO()
with open('resume1.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string)
print(output_string.getvalue().strip())

from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

pdf_text = extract_text_from_pdf('resume1.pdf')

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

# keywords to find for experience
exp_keywords_to_search = ['assisted', 'coordinated', 'intern', 'tutor']
exp_found_keywords = find_experience_keywords(pdf_text, exp_keywords_to_search)

def rank_exp(): 
    if 'intern' in exp_found_keywords:
        global points
        points += 3
    if 'coordinated' in exp_found_keywords:
        points += 2
    if 'assisted' in exp_found_keywords:
        points += 1
    if 'tutor' in exp_found_keywords:
        points += 2
rank_exp()

if exp_found_keywords:
    print("Experience keywords found:", exp_found_keywords)
else:
    print("No keywords found.")


def find_years_keywords(text, keywords):
    found_yrs_keywords = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_yrs_keywords.append(keyword)
    return found_yrs_keywords

yrs_keywords_to_search = ['worked for', 'years of experience', 'over', 'more than']
yrs_found_keywords = find_years_keywords(pdf_text, yrs_keywords_to_search)

if yrs_found_keywords:
    print("Years keywords found:", yrs_found_keywords)
else:
    print("No keywords found.")
# prints points Fuck you vincentFuck you vincentFuck you vincentFuck you vincent
print(f'Points: {points}')

