#imports pdf
import pdfminer
print(pdfminer.__version__)  
points = [0, 0, 0, 0, 0, 0]
index = 1
keywords = []
import re
import os
import glob
from io import StringIO
from pdfminer.high_level import extract_text_to_fp
output_string = StringIO()
from pdfminer.high_level import extract_text

# Define the directory containing the PDF files
directory_path = 'pdf-folder'

# Use glob to find all PDF files in the directory
pdf_files = glob.glob(os.path.join(directory_path, '*.pdf'))

# Loop through each PDF file and process it with pdfminer
for pdf_file in pdf_files:
    try:
        # Extract text from the PDF file
        text = extract_text(pdf_file)
        
        # Process the extracted text (for example, print it or save it to a file)
        print(f"Text from {pdf_file}:\n{text}\n")
        
        # Optionally, save the extracted text to a new file
        output_file = os.path.splitext(pdf_file)[0] + '.txt'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
            
    except Exception as e:
        print(f"An error occurred while processing {pdf_file}: {e}")
print("Processing complete.")


# finds keywords
def find_ed_keywords(text, keywords):
    found_ed_keywords = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_ed_keywords.append(keyword)
    return found_ed_keywords
find_ed_keywords(text, keywords)


# keywords to find
ed_keywords_to_search = ['university', 'degree', 'college', 'major', 'minor', 'trade school', 'high school']
ed_found_keywords = find_ed_keywords(pdf_file, ed_keywords_to_search)

# message to say if keywords are found
if ed_found_keywords:
    print("Keywords found:", ed_found_keywords)
else:
    print("No keywords found.")

# rank keywords related to education
def rank_ed(): 
    if 'university' in ed_found_keywords:
        global points
        points[index] += 2
    if 'degree' in ed_found_keywords:
        points[index] += 2
    if 'college' in ed_found_keywords:
        points[index] += 1
    if 'major' in ed_found_keywords:
        points[index] += 1
    if 'minor' in ed_found_keywords:
        points[index] += 1
    if 'trade school' in ed_found_keywords:
        points[index] += 0.5
    if 'major' in ed_found_keywords:
        points[index] += 0.25
rank_ed()

def find_experience_keywords(text, keywords):
    found_exp_keywords = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_exp_keywords.append(keyword)
    return found_exp_keywords
find_experience_keywords(text, keywords)

# keywords to find for experience
exp_keywords_to_search = ['assisted', 'coordinated', 'intern', 'tutor','teacher', 'leadership']
exp_found_keywords = find_experience_keywords(pdf_file, exp_keywords_to_search)

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
    if 'leadership' in exp_found_keywords:
        points += 1
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
find_skills_keywords(text, keywords)

skills_keywords_to_search = ['python', 'java', 'c++', 'javascript', 'github', 'html', 'css', 'SQL', 'NoSQL', 'SDLC', 'Scrum', 'Kanban', 'AWS', 'Azure', 'iOS', 'Android', 'Linux', 'Windows']
skills_found_keywords = find_skills_keywords(pdf_file, skills_keywords_to_search)

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
    print("Skills found:", skills_found_keywords)
else:
    print("No keywords found.")

for pdf_file in pdf_files: 
    index += 1 
    find_ed_keywords(text, keywords)
    rank_ed()
    find_experience_keywords(text, keywords)
    rank_exp()
    find_skills_keywords(text, keywords)
    find_skills()



# prints points Fuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincentFuck you vincent
print(f'Points: {points}')

