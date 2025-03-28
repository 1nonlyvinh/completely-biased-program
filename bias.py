#imports pdf
import pdfminer
print(pdfminer.__version__)   
points = 0
import re

#opens & reads fake-resume.pdf
from pdfminer.high_level import extract_text
from io import StringIO
from pdfminer.high_level import extract_text_to_fp
output_string = StringIO()
with open('resume1.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string)
print(output_string.getvalue().strip())
 
pdf_text = extract_text('resume1.pdf')
pdf_path = extract_text('resume1.pdf')

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

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
exp_keywords_to_search = ['assisted', 'coordinated', 'intern', 'tutor','teacher', 'leadership']
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

skills_keywords_to_search = ['python', 'java', 'c++', 'javascript', 'github', 'html', 'css', 'SQL', 'NoSQL', 'SDLC', 'Scrum', 'Kanban', 'AWS', 'Azure', 'iOS', 'Android', 'Linux', 'Windows']
skills_found_keywords = find_skills_keywords(pdf_text, skills_keywords_to_search)

def find_skills():
    if 'python' in skills_found_keywords:
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

 # prints points Fuck you vincentFuck you vincentFuck you vincentFuck you vincent
print(f'Points for Resume 1: {points}')

points2 = 0 

with open('resume2.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string)
print(output_string.getvalue().strip())
 
pdf_text = extract_text('resume2.pdf')
pdf_path = extract_text('resume2.pdf')

def extract_text_from_pdf2(pdf_path):
    return extract_text(pdf_path)

# finds keywords
def find_ed_keywords2(text, keywords):
    found_ed_keywords2 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_ed_keywords.append(keyword)
    return found_ed_keywords

# keywords to find
ed_keywords_to_search2 = ['university', 'degree', 'college', 'major', 'minor', 'trade school', 'high school']
ed_found_keywords2 = find_ed_keywords(pdf_text, ed_keywords_to_search)

 # message to say if keywords are found
if ed_found_keywords2:
    print("Keywords found:", ed_found_keywords)
else:
    print("No keywords found.")
 
 # rank keywords related to education 
def rank_ed2():
    if 'university' in ed_found_keywords:
        global points2
        points2 += 2
    if 'degree' in ed_found_keywords:
        points2 += 2
    if 'college' in ed_found_keywords:
        points2 += 1
    if 'major' in ed_found_keywords:
        points2 += 1
    if 'minor' in ed_found_keywords:
        points2 += 1
    if 'trade school' in ed_found_keywords:
        points2 += 0.5
    if 'major' in ed_found_keywords:
        points2 += 0.25
rank_ed2()
 
def find_experience_keywords2(text, keywords):
    found_exp_keywords2 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_exp_keywords.append(keyword)
    return found_exp_keywords2
 
 # keywords to find for experience
exp_keywords_to_search2 = ['assisted', 'coordinated', 'intern', 'tutor','teacher', 'leadership']
exp_found_keywords2 = find_experience_keywords(pdf_text, exp_keywords_to_search)

def rank_exp2():
    if 'intern' in exp_found_keywords:
        global points2
        points2 += 3
    if 'coordinated' in exp_found_keywords:
        points2 += 2
    if 'assisted' in exp_found_keywords:
        points2 += 1
    if 'tutor' in exp_found_keywords:
        points2 += 2
    if 'leadership' in exp_found_keywords:
        points2 += 1
rank_exp2()
 
if exp_found_keywords2:
    print("Experience keywords found:", exp_found_keywords2)
else:
    print("No keywords found.")

def find_skills_keywords2(text, keywords):
    found_skill_keywords2 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_skill_keywords.append(keyword)
    return found_skill_keywords

skills_keywords_to_search2 = ['python', 'java', 'c++', 'javascript', 'github', 'html', 'css', 'SQL', 'NoSQL', 'SDLC', 'Scrum', 'Kanban', 'AWS', 'Azure', 'iOS', 'Android', 'Linux', 'Windows']
skills_found_keywords2 = find_skills_keywords(pdf_text, skills_keywords_to_search)

def find_skills2():
    if 'python' in skills_found_keywords2:
        global points2
        points2 += 1
    if 'java' in skills_found_keywords2:
        points2 += 1
    if 'c++' in skills_found_keywords2:
        points2 += 1
    if 'javascript' in skills_found_keywords2:
        points2 += 1
    if 'html' in skills_found_keywords2:
        points2 += 1
    if 'css' in skills_found_keywords2:
        points2 += 1
    if 'SQL' in skills_found_keywords2:
        points2 += 1
    if 'Scrum' in skills_found_keywords2:
        points2 += 1
    if 'KanBan' in skills_found_keywords2:
        points2 += 1
    if 'AWS' in skills_found_keywords2:
        points2 += 1
    if 'Azure' in skills_found_keywords2:
        points2 += 1
    if 'iOS' in skills_found_keywords2:
        points2 += 1
    if 'Android' in skills_found_keywords2:
        points2 += 1
    if 'Linux' in skills_found_keywords2:
        points2 += 1
    if 'Win' in skills_found_keywords2:
        points2 += 1
find_skills2()

if skills_found_keywords2:
    print("Skills found:", skills_found_keywords2)
else:
    print("No keywords found.")

 
 # prints points Fuck you vincentFuck you vincentFuck you vincentFuck you vincent
print(f'Points for Resume 2: {points2}')

points3 = 0 

with open('resume3.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string)
print(output_string.getvalue().strip())
 
pdf_text = extract_text('resume3.pdf')
pdf_path = extract_text('resume3.pdf')

def extract_text_from_pdf3(pdf_path):
    return extract_text(pdf_path)

# finds keywords
def find_ed_keywords3(text, keywords):
    found_ed_keywords3 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_ed_keywords.append(keyword)
    return found_ed_keywords

# keywords to find
ed_keywords_to_search3 = ['university', 'degree', 'college', 'major', 'minor', 'trade school', 'high school']
ed_found_keywords3 = find_ed_keywords(pdf_text, ed_keywords_to_search)

 # message to say if keywords are found
if ed_found_keywords3:
    print("Keywords found:", ed_found_keywords3)
else:
    print("No keywords found.")
 
 # rank keywords related to education 
def rank_ed3():
    if 'university' in ed_found_keywords:
        global points3
        points3 += 2
    if 'degree' in ed_found_keywords:
        points3 += 2
    if 'college' in ed_found_keywords:
        points3 += 1
    if 'major' in ed_found_keywords:
        points3 += 1
    if 'minor' in ed_found_keywords:
        points3 += 1
    if 'trade school' in ed_found_keywords:
        points3 += 0.5
    if 'major' in ed_found_keywords:
        points3 += 0.25
rank_ed3()
 
def find_experience_keywords3(text, keywords):
    found_exp_keywords3 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_exp_keywords.append(keyword)
    return found_exp_keywords3
 
 # keywords to find for experience
exp_keywords_to_search3 = ['assisted', 'coordinated', 'intern', 'tutor','teacher', 'leadership']
exp_found_keywords3 = find_experience_keywords(pdf_text, exp_keywords_to_search)

def rank_exp3():
    if 'intern' in exp_found_keywords:
        global points3
        points3 += 3
    if 'coordinated' in exp_found_keywords:
        points3 += 2
    if 'assisted' in exp_found_keywords:
        points3 += 1
    if 'tutor' in exp_found_keywords:
        points3 += 2
    if 'leadership' in exp_found_keywords:
        points3 += 1
rank_exp2()
 
if exp_found_keywords3:
    print("Experience keywords found:", exp_found_keywords3)
else:
    print("No keywords found.")

def find_skills_keywords3(text, keywords):
    found_skill_keywords3 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_skill_keywords.append(keyword)
    return found_skill_keywords

skills_keywords_to_search3 = ['python', 'java', 'c++', 'javascript', 'github', 'html', 'css', 'SQL', 'NoSQL', 'SDLC', 'Scrum', 'Kanban', 'AWS', 'Azure', 'iOS', 'Android', 'Linux', 'Windows']
skills_found_keywords3 = find_skills_keywords(pdf_text, skills_keywords_to_search)

def find_skills3():
    if 'python' in skills_found_keywords2:
        global points3
        points3 += 1
    if 'java' in skills_found_keywords2:
        points3 += 1
    if 'c++' in skills_found_keywords2:
        points3 += 1
    if 'javascript' in skills_found_keywords2:
        points3 += 1
    if 'html' in skills_found_keywords2:
        points3 += 1
    if 'css' in skills_found_keywords2:
        points3 += 1
    if 'SQL' in skills_found_keywords2:
        points3 += 1
    if 'Scrum' in skills_found_keywords2:
        points3 += 1
    if 'KanBan' in skills_found_keywords2:
        points3 += 1
    if 'AWS' in skills_found_keywords2:
        points3 += 1
    if 'Azure' in skills_found_keywords2:
        points3 += 1
    if 'iOS' in skills_found_keywords2:
        points3 += 1
    if 'Android' in skills_found_keywords2:
        points3 += 1
    if 'Linux' in skills_found_keywords2:
        points3 += 1
    if 'Win' in skills_found_keywords2:
        points3 += 1
find_skills3()

if skills_found_keywords3:
    print("Skills found:", skills_found_keywords3)
else:
    print("No keywords found.")

 
 # prints points Fuck you vincentFuck you vincentFuck you vincentFuck you vincent
print(f'Points for Resume 3: {points3}')