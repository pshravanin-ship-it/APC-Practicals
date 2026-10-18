# 1.
import re


text = "My age is 20 and marks are 95"
print("1. Digits:", re.findall(r'\d', text))


# 2.
import re
sentence = "orange and apple are amazing fruits"
print("2. Words starting with A or a:", re.findall(r'\b[Aa]\w*', sentence))


# 3.
import re
text = "Hello python programming"
vowels = re.findall(r'[aeiou]', text, re.IGNORECASE)
print("3. Total vowels:", len(vowels))


# 4.
import re
text = "Hello PYTHON World"
print("4. Uppercase letters:", re.findall(r'[A-Z]', text))

# 5.
import re
text = "Hello World\nPython\tProgramming"

print("5. Spaces:", len(re.findall(r' ', text)))
print("   Tabs:", len(re.findall(r'\t', text)))
print("   Newlines:", len(re.findall(r'\n', text)))

#6.	
import re
text = "This   is  a    text with   multiple spaces."
replaced_text = re.sub(r'\s+', ' ', text)
print(" Replaced text:", replaced_text)

#7.
import re
sentence = "Hello world, this is a simple sentence with five-character words."
five_char_words = re.findall(r'\b\w{5}\b', sentence)
print("Words with exactly five characters:", five_char_words)

# 8.
import re
text = "Cats dogs birds and books"
print("Words ending with s:", re.findall(r'\b\w*s\b', text, re.IGNORECASE))


# 9. 
import re
text = "Hello@123! Python# is$ easy."
result = re.sub(r'[^a-zA-Z0-9 ]', '', text)
print("After removing special characters:", result)


# 10. 
import re
sentence = "German is easy to learn"
words = re.findall(r'\b\w+\b', sentence)
print(" Number of words:", len(words))


# 11. 
import re
mobile = input("Enter a mobile number: ")

if re.fullmatch(r'[6-9]\d{9}', mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")


# 12. 
import re
email = input("Enter an email address: ")

if re.fullmatch(r'[\w.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email):
    print("Valid email address")
else:
    print("Invalid email address")


# 13. 
import re
text = "Dates are 5-08-2006 and 26-01-2026"
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
print("Dates:", dates)


# 14. 
import re
text = "Visit https://google.com and http://example.com"
urls = re.findall(r'https?://[^\s]+', text)
print("Web addresses:", urls)


# 15.
import re
post = "Love #Python and #Programming! #Coding2026"
hashtags = re.findall(r'#[A-Za-z0-9_]+', post)
print("Hashtags:", hashtags)

# 16. 
import re
password = input(" Enter a password: ")

pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}'

if re.fullmatch(pattern, password):
    print("Strong password")
else:
    print("Weak password")


# 17. 
import re
sentence = "Python is is easy and AND useful"
repeated = re.findall(r'\b(\w+)\s+\1\b', sentence, re.IGNORECASE)
print("Repeated words:", repeated)


# 18. 
import re
text = "My PIN is 411001 and another PIN is 560001"
pin_codes = re.findall(r'\b[1-9]\d{5}\b', text)
print(" PIN codes:", pin_codes)


# 19. 
import re
vehicle = input(" Enter vehicle number (e.g. MH12AB1234): ")

pattern = r'[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}'

if re.fullmatch(pattern, vehicle.upper()):
    print("Valid vehicle number format")
else:
    print("Invalid vehicle number format")


# 20. 
import re
text = "Files: photo.jpg notes.txt program.py document.pdf"
extensions = re.findall(r'\b[\w-]+\.(\w+)\b', text)
print("File extensions:", extensions)

#21.	
import re
text = "<p>Hello, <b>world!</b> This is a <i>sample</i> text with <a href='#'>HTML</a> tags.</p>"
cleaned_text = re.sub(r'<.*?>', '', text)
cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
cleaned_text=re.sub(r'[^\w\s]', '', cleaned_text)
print("Cleaned text:", cleaned_text.strip())

#22.	
import re
invoixe_text = "Invoice No: INV-2023-001, Date: 2023-08-15, Amount: $1500.00"
invoice_number = re.search(r'Invoice No:\s*(\S+)', invoixe_text)
date = re.search(r'Date:\s*(\d{4}-\d{2}-\d{2})', invoixe_text)
amount = re.search(r'Amount:\s*\$(\d+\.\d+)', invoixe_text)
print("Invoice Number:", invoice_number.group(1) if invoice_number else "Not found")
print("Date:", date.group(1) if date else "Not found")
print("Amount:", amount.group(1) if amount else "Not found")


# 23. 
import re
code = '''
x = 10  # This is a comment
# This is also a comment
print("Hello")
'''
comments = re.findall(r'#.*', code)
print("Single-line comments:", comments)


# 24. 
import re
product = input(" Enter product code (ABC-1234-XY): ")
pattern = r'[A-Z]{3}-\d{4}-[A-Z]{2}'
if re.fullmatch(pattern, product):
    print("Valid product code")
else:
    print("Invalid product code")


# 25. 
import re
text = """
Name: Shravani, Roll: 101, Marks: 85
Name: Piyusha, Roll: 102, Marks: 92
Name: Vaishanvi, Roll: 103, Marks: 78
"""
pattern = r'Name:\s*(\w+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)'
students = re.findall(pattern, text)
print(" Student details:")
for name, roll, marks in students:
    print("Name:", name, "Roll:", roll, "Marks:", marks)


# 26. 
import re
text = """
Research paper (2024), DOI: 10.1234/abcd.5678
Email: author@example.com
URL: https://example.com/paper
Another paper (2022), DOI: 10.5678/xyz.1234
Email: researcher@gmail.com
URL: http://research.org/article
"""
dois = re.findall(r'\b10\.\d{4,9}/[^\s,]+', text)
years = re.findall(r'\b(?:19|20)\d{2}\b', text)
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.[A-Za-z]{2,}\b', text)
urls = re.findall(r'https?://[^\s]+', text)
print("DOIs:", dois)
print("Publication years:", years)
print("Email addresses:", emails)
print("URLs:", urls)