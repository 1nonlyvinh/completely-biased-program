#imports pdf
import pdfminer
print(pdfminer.__version__)  
points = 0
import re
import os

pdf_directory = 'pdf-folder'

for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        
        # Extract text from the PDF
        try:
            text = extract_text(pdf_path)
            print(f"Content of {filename}:\n{text}\n")
        except Exception as e:
            print(f"An error occurred while processing {filename}: {e}")

#opens & reads fake-resume.pdf

from io import StringIO
from pdfminer.high_level import extract_text_to_fp
output_string = StringIO()
with open('resume6.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string)
print(output_string.getvalue().strip())

from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


pdf_text = extract_text_from_pdf('resume6.pdf')

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
exp_keywords_to_search = ['assisted', 'coordinated', 'intern', 'tutor','teacher']
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

def find_skills_keywords(text, keywords):
    found_skill_keywords = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_skill_keywords.append(keyword)
    return found_skill_keywords

skills_keywords_to_search = ['python', 'java', 'c++', 'javascript', 'html', 'css', 'SQL', 'NoSQL', 'SDLC', 'Scrum', 'Kanban', 'AWS', 'Azure', 'iOS', 'Android', 'Linux', 'Windows']
skills_found_keywords = find_skills_keywords(pdf_text, skills_keywords_to_search)

def find_skills(): 
    if 'pyhton' in skills_found_keywords:
        global points
        points += 1
    if 'java' in skills_found_keywords:
        points += 1
    if 'c++' in skills_found_keywords:
        points += 1
    if 'javascript' in skills_found_keywords:
        points += 1
    if 'html' in skills_found_keywords:
        points += 1
    if 'css' in skills_found_keywords:
        points += 1
    if 'SQL' in skills_found_keywords:
        points += 1
    if 'Scrum' in skills_found_keywords:
        points += 1
    if 'KanBan' in skills_found_keywords:
        points += 1
    if 'AWS' in skills_found_keywords:
        points += 1
    if 'Azure' in skills_found_keywords:
        points += 1
    if 'iOS' in skills_found_keywords:
        points += 1
    if 'Android' in skills_found_keywords:
        points += 1
    if 'Linux' in skills_found_keywords:
        points += 1
    if 'Win' in skills_found_keywords:
        points += 1
find_skills()
if skills_found_keywords:
    print("Skills foun:", skills_found_keywords)
else:
    print("No keywords found.")


# prints points Fuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincent
print(f'Points: {points}')

