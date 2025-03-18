import pdfminer
print(pdfminer.__version__)  

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

def find_keywords(text, keywords):
    found_keywords = []
    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_keywords.append(keyword)
    return found_keywords

keywords_to_search = ['the', 'scoobydoo', 'hi', 'accomplishments']
found_keywords = find_keywords(pdf_text, keywords_to_search)


if found_keywords:
    print("Keywords found:", found_keywords)
else:
    print("No keywords found.")
