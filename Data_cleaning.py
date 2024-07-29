import sqlite3
import pandas as pd
import zipfile
import os
import re
from html import unescape
import json

# Path to your .apkg file
apkg_path = 'P:/Program Files/Python_programs/Study App/Anki Exports/export.colpkg'
extract_to_folder = 'P:/Program Files/Python_programs/Study App/Anki Exports'

# Extract the .apkg file
with zipfile.ZipFile(apkg_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_folder)

print("Files extracted:", os.listdir(extract_to_folder))
# Path to the SQLite database extracted from the .apkg
db_path = os.path.join(extract_to_folder, 'P:/Program Files/Python_programs/Study App/Anki Exports/collection.anki21')

# Connect to the SQLite database
conn = sqlite3.connect(db_path)

query = """
SELECT cards.id, cards.ivl, notes.flds, notes.sfld
FROM cards
INNER JOIN notes ON cards.id = notes.id
WHERE cards.ivl = 1
Order BY cards.ivl ASC ;"""
df = pd.read_sql_query(query, conn)
df.to_csv('P:/Program Files/Python_programs/Study App/Filter/cards.csv', encoding='utf-8')

# Close the connection
conn.close()

def contains_korean(text):
    # Regex to detect Hangul characters
    return bool(re.search(r'[\uAC00-\uD7AF]', text))

# Function to filter DataFrame for rows containing Korean
def filter_korean_cards(df, column_name='flds'):
    return df[df[column_name].apply(contains_korean)]

# Applying the filter to include only entries with Korean text
filtered_df = filter_korean_cards(df, 'flds')

# Optionally save the filtered data to a CSV file
filtered_df.to_csv('P:/Program Files/Python_programs/Study App/Filter/cards_filtered.csv', index=False, encoding='utf-8')

### print("Filtered DataFrame with Korean text:")
### print(filtered_df.head())

def extract_korean(text):
    # Split the text by the delimiter
    fields = text.split('\x1f')  # \x1f is the ASCII Unit Separator
    # Use regex to filter out only segments with Korean characters
    korean_text = [field for field in fields if re.search("[가-힣]+", field)]
    # Join the Korean segments into a single string separated by spaces
    return ' '.join(korean_text)

def clean_korean_text(text):
    ### print("Original Text:", text)
    # Decode HTML entities
    text = unescape(text)
    # Remove all HTML tags and contents within
    text = re.sub(r"<[^>]*>", "", text)
    # Remove URLs, sound references, and any JavaScript or similar
    text = re.sub(r'https?:\/\/\S+|\[sound:[^\]]+\]', '', text)
    # Use the first valid Korean phrase and ignore subsequent duplicative information
    text = re.sub(r'[^가-힣\s].*$', '', text)  # Stop at first non-Korean character sequence
    # Remove any trailing English or special characters often included in annotations
    text = re.sub(r'[a-zA-Z0-9\[\]\(\)\{\}:;,.?!_\-]', '', text)
    # Normalize spaces
    text = re.sub(r'\s+', ' ', text).strip()
    ### print("Cleaned Text:", text) # Prints cleaned text to console
    return text

def clean_specific_card(text):
    # Split the text by the '' character and extract the segment of interest
    parts = text.split('')
    if len(parts) > 2:
        return parts[1]  # Return the content between the first and second ''
    return ""  # Return an empty string if the format is unexpected

def extract_and_clean(df, text_column='flds'):
    cleaned_texts = []  # List to hold all cleaned texts
    for index, row in df.iterrows():
        card_text = row[text_column]
        if re.search(r'^\d+', card_text):
            clean_card = clean_specific_card(card_text)
        else:
            korean_card_text = extract_korean(card_text)  # Apply extract_korean only if not starting with a number
            clean_card = clean_korean_text(korean_card_text)
        cleaned_texts.append(clean_card)  # Append cleaned text to the list
        df.at[index, 'cleaned_text'] = clean_card  # Add/Update the cleaned_text column in the DataFrame

    return df, cleaned_texts  # Return the updated DataFrame and the list of cleaned texts


# Load the dataset
data_path = 'P:/Program Files/Python_programs/Study App/Filter/cards_filtered.csv'
data = pd.read_csv(data_path)

## Check the data to ensure it's loaded correctly
# print("Data loaded with columns:", data.columns.tolist())
# print("Sample data:", data.head())

# Apply the extraction and cleaning functions
processed_df, cleaned_texts = extract_and_clean(data, 'flds')

# Now check what's inside processed_df and cleaned_texts
###print("Processed DataFrame:")
###print(processed_df.head())
###print("Sample of cleaned texts:", cleaned_texts[:5])

# Proceed to save the data as before
processed_df.to_csv('P:/Program Files/Python_programs/Study App/Filter/cleaned_dataframe.csv', index=False, encoding='utf-8')

with open('P:/Program Files/Python_programs/Study App/Filter/cleaned_korean_text.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_texts, f, ensure_ascii=False, indent=4)

print("Data has been processed and saved.")
