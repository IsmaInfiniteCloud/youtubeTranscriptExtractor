import re

def clean_transcript(text):
    # Regular expression to match the timestamp pattern
    # Here, \n? tries to match a newline before the timestamp if it's there.
    pattern = r'\n?\d{1,2}:\d{2}\s*'
    # Using space to replace the matched pattern
    return re.sub(pattern, ' ', text).strip()

# Read the source text
with open('source.txt', 'r') as source_file:
    text = source_file.read()

# Clean the text
cleaned_text = clean_transcript(text)

# Write the cleaned text to result.txt
with open('result.txt', 'w') as result_file:
    result_file.write(cleaned_text)
