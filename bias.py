import pdfminer
print(pdfminer.__version__)  
points = 0

from io import StringIO
from pdfminer.high_level import extract_text_to_fp
output_string = StringIO()
with open('fake-resume.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string)
print(output_string.getvalue().strip())

from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

pdf_text = extract_text_from_pdf('fake-resume.pdf')

def find_ed_keywords(text, keywords):
    found_ed_keywords = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_ed_keywords.append(keyword)
    return found_ed_keywords

keywords_to_search = ['university', 'degree', 'college', 'major', 'minor', 'trade school', 'high school']
found_keywords = find_ed_keywords(pdf_text, keywords_to_search)


if found_keywords:
    print("Keywords found:", found_keywords)
else:
    print("No keywords found.")

def rank_ed(): 
    if 'degree' in found_keywords or 'college'  in found_keywords:
        global points
        points += 2

rank_ed()

print(f'Points: {points}')