#imports pdf
import pdfminer
print(pdfminer.__version__)   
points = 0
import re
import time
#opens & reads fake-resume.pdf
from pdfminer.high_level import extract_text
from io import StringIO
from pdfminer.high_level import extract_text_to_fp
output_string = StringIO()
with open('resume1.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string)
print(output_string.getvalue().strip())

#extract text
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
 
# finds keywords related to experience
def find_experience_keywords(text, keywords):
    found_exp_keywords = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_exp_keywords.append(keyword)
    return found_exp_keywords
 
 # keywords to find for experience
exp_keywords_to_search = ['assisted', 'coordinated', 'intern', 'tutor','teacher', 'leadership']
exp_found_keywords = find_experience_keywords(pdf_text, exp_keywords_to_search)

#assigns points based on what experience keywords are found
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

# displays found keywords
if exp_found_keywords:
    print("Experience keywords found:", exp_found_keywords)
else:
    print("No keywords found.")

#finds skill-related keywords
def find_skills_keywords(text, keywords):
    found_skill_keywords = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_skill_keywords.append(keyword)
    return found_skill_keywords

#keywords to find
skills_keywords_to_search = ['python', 'java', 'c++', 'javascript', 'github', 'html', 'css', 'SQL', 'NoSQL', 'SDLC', 'Scrum', 'Kanban', 'AWS', 'Azure', 'iOS', 'Android', 'Linux', 'Windows', 'postman']
skills_found_keywords = find_skills_keywords(pdf_text, skills_keywords_to_search)

# assigns points on skills
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
    if 'postman' in skills_found_keywords:
        points += 1
find_skills()

# displays what skills keywords are found
if skills_found_keywords:
    print("Skills found:", skills_found_keywords)
else:
    print("No keywords found.")

# prints points 
print(f'Points for Resume 1: {points}')

points2 = 0 

# extract text from resume 2
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
    print("Keywords found:", ed_found_keywords2)
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

# finds experience keywords
def find_experience_keywords2(text, keywords):
    found_exp_keywords2 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_exp_keywords.append(keyword)
    return found_exp_keywords2
 
 # keywords to find for experience
exp_keywords_to_search2 = ['assisted', 'coordinated', 'intern', 'tutor','teacher', 'leadership']
exp_found_keywords2 = find_experience_keywords(pdf_text, exp_keywords_to_search)

# assigns points for keywords found
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
 
# displays keywords found
if exp_found_keywords2:
    print("Experience keywords found:", exp_found_keywords2)
else:
    print("No keywords found.")

# find skills keywords
def find_skills_keywords2(text, keywords):
    found_skill_keywords2 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_skill_keywords.append(keyword)
    return found_skill_keywords

# list of skills keywords
skills_keywords_to_search2 = ['python', 'java', 'c++', 'javascript', 'github', 'html', 'css', 'SQL', 'NoSQL', 'SDLC', 'Scrum', 'Kanban', 'AWS', 'Azure', 'iOS', 'Android', 'Linux', 'Windows', 'postman']
skills_found_keywords2 = find_skills_keywords(pdf_text, skills_keywords_to_search)

# assigns points to points 2 var
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
    if 'postman' in skills_found_keywords2:
        points2 += 1
find_skills2()

# displays what keywords are found 2nd pdf
if skills_found_keywords2:
    print("Skills found:", skills_found_keywords2)
else:
    print("No keywords found.")

 # prints points
print(f'Points for Resume 2: {points2}')

points3 = 0 

# extracts pdf 3
with open('resume3.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string)
print(output_string.getvalue().strip())
 
pdf_text = extract_text('resume3.pdf')
pdf_path = extract_text('resume3.pdf')

def extract_text_from_pdf3(pdf_path):
    return extract_text(pdf_path)

# finds keywords ed
def find_ed_keywords3(text, keywords):
    found_ed_keywords3 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_ed_keywords.append(keyword)
    return found_ed_keywords

# keywords to find ed
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
 
 # finds experience keywords, pdf 3
def find_experience_keywords3(text, keywords):
    found_exp_keywords3 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_exp_keywords.append(keyword)
    return found_exp_keywords3
 
 # keywords to find for experience
exp_keywords_to_search3 = ['assisted', 'coordinated', 'intern', 'tutor','teacher', 'leadership']
exp_found_keywords3 = find_experience_keywords(pdf_text, exp_keywords_to_search)

# assigns points 
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
rank_exp3()
 
# displays keywords found
if exp_found_keywords3:
    print("Experience keywords found:", exp_found_keywords3)
else:
    print("No keywords found.")

# finds skills keywords
def find_skills_keywords3(text, keywords):
    found_skill_keywords3 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_skill_keywords.append(keyword)
    return found_skill_keywords

# skills keywords to search for
skills_keywords_to_search3 = ['python', 'java', 'c++', 'javascript', 'github', 'html', 'css', 'SQL', 'NoSQL', 'SDLC', 'Scrum', 'Kanban', 'AWS', 'Azure', 'iOS', 'Android', 'Linux', 'Windows', 'postman']
skills_found_keywords3 = find_skills_keywords(pdf_text, skills_keywords_to_search)

# assigns points 
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
    if 'postman' in skills_found_keywords:
        points3 += 1
find_skills3()

# displays s
if skills_found_keywords3:
    print("Skills found:", skills_found_keywords3)
else:
    print("No keywords found.")

 
 # prints points 
print(f'Points for Resume 3: {points3}')


points4 = 0 

with open('resume4.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string)
print(output_string.getvalue().strip())
 
pdf_text = extract_text('resume4.pdf')
pdf_path = extract_text('resume4.pdf')

def extract_text_from_pdf4(pdf_path):
    return extract_text(pdf_path)

# finds keywords
def find_ed_keywords4(text, keywords):
    found_ed_keywords4 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_ed_keywords.append(keyword)
    return found_ed_keywords

# keywords to find
ed_keywords_to_search4 = ['university', 'degree', 'college', 'major', 'minor', 'trade school', 'high school']
ed_found_keywords4 = find_ed_keywords(pdf_text, ed_keywords_to_search)

 # message to say if keywords are found
if ed_found_keywords4:
    print("Keywords found:", ed_found_keywords4)
else:
    print("No keywords found.")
 
 # rank keywords related to education 
def rank_ed4():
    if 'university' in ed_found_keywords:
        global points4
        points4 += 2
    if 'degree' in ed_found_keywords:
        points4 += 2
    if 'college' in ed_found_keywords:
        points4 += 1
    if 'major' in ed_found_keywords:
        points4 += 1
    if 'minor' in ed_found_keywords:
        points4 += 1
    if 'trade school' in ed_found_keywords:
        points4 += 0.5
    if 'major' in ed_found_keywords:
        points4 += 0.25
rank_ed4()
 
def find_experience_keywords4(text, keywords):
    found_exp_keywords4 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_exp_keywords.append(keyword)
    return found_exp_keywords4
 
 # keywords to find for experience
exp_keywords_to_search4 = ['assisted', 'coordinated', 'intern', 'tutor','teacher', 'leadership']
exp_found_keywords4 = find_experience_keywords(pdf_text, exp_keywords_to_search)

# assigns points
def rank_exp4():
    if 'intern' in exp_found_keywords:
        global points4
        points4 += 3
    if 'coordinated' in exp_found_keywords:
        points4 += 2
    if 'assisted' in exp_found_keywords:
        points4 += 1
    if 'tutor' in exp_found_keywords:
        points4 += 2
    if 'leadership' in exp_found_keywords:
        points4 += 1
rank_exp4()
 
 # displays keywords found
if exp_found_keywords4:
    print("Experience keywords found:", exp_found_keywords4)
else:
    print("No keywords found.")

# keywords to find skills pdf 4 
def find_skills_keywords4(text, keywords):
    found_skill_keywords4 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_skill_keywords.append(keyword)
    return found_skill_keywords

# list of keywords to search
skills_keywords_to_search4 = ['python', 'java', 'c++', 'javascript', 'github', 'html', 'css', 'SQL', 'NoSQL', 'SDLC', 'Scrum', 'Kanban', 'AWS', 'Azure', 'iOS', 'Android', 'Linux', 'Windows', 'postman']
skills_found_keywords4 = find_skills_keywords(pdf_text, skills_keywords_to_search)

# find skills 
def find_skills4():
    if 'python' in skills_found_keywords2:
        global points4
        points4 += 1
    if 'java' in skills_found_keywords2:
        points4 += 1
    if 'c++' in skills_found_keywords2:
        points4 += 1
    if 'javascript' in skills_found_keywords2:
        points4 += 1
    if 'html' in skills_found_keywords2:
        points4 += 1
    if 'css' in skills_found_keywords2:
        points4 += 1
    if 'SQL' in skills_found_keywords2:
        points4 += 1
    if 'Scrum' in skills_found_keywords2:
        points4 += 1
    if 'KanBan' in skills_found_keywords2:
        points4 += 1
    if 'AWS' in skills_found_keywords2:
        points4 += 1
    if 'Azure' in skills_found_keywords2:
        points4 += 1
    if 'iOS' in skills_found_keywords2:
        points4 += 1
    if 'Android' in skills_found_keywords2:
        points4 += 1
    if 'Linux' in skills_found_keywords2:
        points4 += 1
    if 'Win' in skills_found_keywords2:
        points4 += 1
    if 'postman' in skills_found_keywords:
        points4 += 1
find_skills4()

# displays keywords found 
if skills_found_keywords4:
    print("Skills found:", skills_found_keywords4)
else:
    print("No keywords found.")

 
 # prints points 
print(f'Points for Resume 4: {points4}')

points5 = 0 

# extract text resume 5
with open('resume5.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string)
print(output_string.getvalue().strip())
 
pdf_text = extract_text('resume5.pdf')
pdf_path = extract_text('resume5.pdf')

def extract_text_from_pdf5(pdf_path):
    return extract_text(pdf_path)

# finds keywords
def find_ed_keywords5(text, keywords):
    found_ed_keywords5 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_ed_keywords.append(keyword)
    return found_ed_keywords

# keywords to find
ed_keywords_to_search5 = ['university', 'degree', 'college', 'major', 'minor', 'trade school', 'high school']
ed_found_keywords5 = find_ed_keywords(pdf_text, ed_keywords_to_search)

 # message to say if keywords are found
if ed_found_keywords5:
    print("Keywords found:", ed_found_keywords5)
else:
    print("No keywords found.")
 
 # rank keywords related to education on pdf 5
def rank_ed5():
    if 'university' in ed_found_keywords:
        global points5
        points5 += 2
    if 'degree' in ed_found_keywords:
        points5 += 2
    if 'college' in ed_found_keywords:
        points5 += 1
    if 'major' in ed_found_keywords:
        points5 += 1
    if 'minor' in ed_found_keywords:
        points5 += 1
    if 'trade school' in ed_found_keywords:
        points5 += 0.5
    if 'major' in ed_found_keywords:
        points5 += 0.25
rank_ed5()

# find exp keywords pdf 5
def find_experience_keywords5(text, keywords):
    found_exp_keywords5 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_exp_keywords.append(keyword)
    return found_exp_keywords5
 
 # keywords to find for experience
exp_keywords_to_search5 = ['assisted', 'coordinated', 'intern', 'tutor','teacher', 'leadership']
exp_found_keywords5 = find_experience_keywords(pdf_text, exp_keywords_to_search)

# assigns points for rank keywords pdf 
def rank_exp5():
    if 'intern' in exp_found_keywords:
        global points5
        points5 += 3
    if 'coordinated' in exp_found_keywords:
        points5 += 2
    if 'assisted' in exp_found_keywords:
        points5 += 1
    if 'tutor' in exp_found_keywords:
        points5 += 2
    if 'leadership' in exp_found_keywords:
        points5 += 1
    
rank_exp5()

# displays experience keywords
if exp_found_keywords5:
    print("Experience keywords found:", exp_found_keywords5)
else:
    print("No keywords found.")

# finds skills keywords
def find_skills_keywords5(text, keywords):
    found_skill_keywords5 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_skill_keywords.append(keyword)
    return found_skill_keywords

# skills keywords to search pdf 5
skills_keywords_to_search5 = ['python', 'java', 'c++', 'javascript', 'github', 'html', 'css', 'SQL', 'NoSQL', 'SDLC', 'Scrum', 'Kanban', 'AWS', 'Azure', 'iOS', 'Android', 'Linux', 'Windows', 'postman']
skills_found_keywords5 = find_skills_keywords(pdf_text, skills_keywords_to_search)

# assigns points based on keywords found
def find_skills5():
    if 'python' in skills_found_keywords2:
        global points5
        points5 += 1
    if 'java' in skills_found_keywords2:
        points5 += 1
    if 'c++' in skills_found_keywords2:
        points5 += 1
    if 'javascript' in skills_found_keywords2:
        points5 += 1
    if 'html' in skills_found_keywords2:
        points5 += 1
    if 'css' in skills_found_keywords2:
        points5 += 1
    if 'SQL' in skills_found_keywords2:
        points5 += 1
    if 'Scrum' in skills_found_keywords2:
        points5 += 1
    if 'KanBan' in skills_found_keywords2:
        points5 += 1
    if 'AWS' in skills_found_keywords2:
        points5 += 1
    if 'Azure' in skills_found_keywords2:
        points5 += 1
    if 'iOS' in skills_found_keywords2:
        points5 += 1
    if 'Android' in skills_found_keywords2:
        points5 += 1
    if 'Linux' in skills_found_keywords2:
        points5 += 1
    if 'Win' in skills_found_keywords2:
        points5 += 1
    if 'postman' in skills_found_keywords:
        points5 += 1
find_skills5()

# displays found keywords
if skills_found_keywords5:
    print("Skills found:", skills_found_keywords5)
else:
    print("No keywords found.")

 
 # prints points 
print(f'Points for Resume 5: {points5}')

points6 = 0 

# extract texts from pdf6 
with open('resume6.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string)
print(output_string.getvalue().strip())
 
pdf_text = extract_text('resume6.pdf')
pdf_path = extract_text('resume6.pdf')

def extract_text_from_pdf6(pdf_path):
    return extract_text(pdf_path)

# finds keywords
def find_ed_keywords6(text, keywords):
    found_ed_keywords6 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_ed_keywords.append(keyword)
    return found_ed_keywords

# keywords to find
ed_keywords_to_search6 = ['university', 'degree', 'college', 'major', 'minor', 'trade school', 'high school']
ed_found_keywords6 = find_ed_keywords(pdf_text, ed_keywords_to_search)

 # message to say if keywords are found
if ed_found_keywords6:
    print("Keywords found:", ed_found_keywords6)
else:
    print("No keywords found.")
 
 # rank keywords related to education 
def rank_ed6():
    if 'university' in ed_found_keywords:
        global points6
        points6 += 2
    if 'degree' in ed_found_keywords:
        points6 += 2
    if 'college' in ed_found_keywords:
        points6 += 1
    if 'major' in ed_found_keywords:
        points6 += 1
    if 'minor' in ed_found_keywords:
        points6 += 1
    if 'trade school' in ed_found_keywords:
        points6 += 0.5
    if 'major' in ed_found_keywords:
        points6 += 0.25
rank_ed6()

# finds experience keywords 6 
def find_experience_keywords6(text, keywords):
    found_exp_keywords6 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_exp_keywords.append(keyword)
    return found_exp_keywords6
 
 # keywords to find for experience
exp_keywords_to_search6 = ['assisted', 'coordinated', 'intern', 'tutor', 'teacher', 'leadership']
exp_found_keywords6 = find_experience_keywords(pdf_text, exp_keywords_to_search)

# assigns points on experience points found
def rank_exp6():
    if 'intern' in exp_found_keywords:
        global points6
        points6 += 3
    if 'coordinated' in exp_found_keywords:
        points6 += 2
    if 'assisted' in exp_found_keywords:
        points6 += 1
    if 'tutor' in exp_found_keywords:
        points6 += 2
    if 'leadership' in exp_found_keywords:
        points6 += 1
rank_exp6()

# displays experience keywords
if exp_found_keywords6:
    print("Experience keywords found:", exp_found_keywords6)
else:
    print("No keywords found.")

# find skills keywords
def find_skills_keywords6(text, keywords):
    found_skill_keywords6 = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_skill_keywords.append(keyword)
    return found_skill_keywords

skills_keywords_to_search6 = ['python', 'java', 'c++', 'javascript', 'github', 'html', 'css', 'SQL', 'NoSQL', 'SDLC', 'Scrum', 'Kanban', 'AWS', 'Azure', 'iOS', 'Android', 'Linux', 'Windows', 'postman']
skills_found_keywords6 = find_skills_keywords(pdf_text, skills_keywords_to_search)

# assigns points of keywords on pdf
def find_skills6():
    if 'python' in skills_found_keywords6:
        global points6
        points6 += 1
    if 'java' in skills_found_keywords6:
        points6 += 1
    if 'c++' in skills_found_keywords6:
        points6 += 1
    if 'javascript' in skills_found_keywords6:
        points6 += 1
    if 'html' in skills_found_keywords6:
        points6 += 1
    if 'css' in skills_found_keywords6:
        points6 += 1
    if 'SQL' in skills_found_keywords2:
        points6 += 1
    if 'Scrum' in skills_found_keywords2:
        points6 += 1
    if 'KanBan' in skills_found_keywords2:
        points6 += 1
    if 'AWS' in skills_found_keywords2:
        points6 += 1
    if 'Azure' in skills_found_keywords2:
        points6 += 1
    if 'iOS' in skills_found_keywords2:
        points6 += 1
    if 'Android' in skills_found_keywords2:
        points6 += 1
    if 'Linux' in skills_found_keywords2:
        points6 += 1
    if 'Win' in skills_found_keywords2:
        points6 += 1
    if 'postman' in skills_found_keywords:
        points6 += 1
find_skills6()

if skills_found_keywords6:
    print("Skills found:", skills_found_keywords6)
else:
    print("No keywords found.")

 
 # prints points Frick you vincent
print(f'Points for Resume 6: {points6}')
 
print(f'Points for eachh Resume: 1: {points} | 2: {points2} | 3: {points3} | 4: {points4} | 5: {points5} | 6: {points6}')
print(f"The greatest amount of points is: 19, so Resume 2 gets the position")
