import csv
import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

# Update file path to point to your cloned sentences.csv file
data_file = 'sentences.csv'

# Read sentences from the data file and preprocess
darija_sentences = []
english_sentences = []

try:
    with open(data_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row if exists
        for row in reader:
            darija_sentences.append(preprocess(row[0].strip()))  # Adjust indexing based on your file structure
            english_sentences.append(preprocess(row[1].strip()))  # Adjust indexing based on your file structure

    # Save preprocessed data
    with open('data/darija_clean.txt', 'w', encoding='utf-8') as f_darija:
        f_darija.writelines('\n'.join(darija_sentences))
    with open('data/english_clean.txt', 'w', encoding='utf-8') as f_english:
        f_english.writelines('\n'.join(english_sentences))

    print("Preprocessing completed.")

except FileNotFoundError:
    print(f"Error: File '{data_file}' not found. Please check the file path.")
except Exception as e:
    print(f"Error: {e}")
