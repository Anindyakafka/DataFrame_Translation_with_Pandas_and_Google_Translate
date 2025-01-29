import pandas as pd
from googletrans import Translator
import time

# Load your DataFrame (assuming it's from an Excel file)
df = pd.read_excel("C:/Users/anind/Downloads/hindi.xlsx")

print("Data before translation:")
print(df.head())

# Initialize the translator
translator = Translator()

# Batch translation function with error handling
def batch_translate(texts, src='hi', dest='en', batch_size=50, retries=3):
    translations = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        for attempt in range(retries):
            try:
                translated_batch = translator.translate(batch, src=src, dest=dest)
                translations.extend([translation.text for translation in translated_batch])
                break
            except Exception as e:
                print(f"Error: {e}. Retrying ({attempt + 1}/{retries})...")
                time.sleep(2)  # Wait before retrying
        else:
            print("Failed to translate batch after multiple attempts.")
            translations.extend([""] * len(batch))  # Add empty translations for failed batch
    return translations

# Translate each column and create new columns with English translations
for column in df.columns:
    df[f'{column}_English'] = batch_translate(df[column].astype(str).tolist())

print("Data after translation:")
print(df.head())

# Save the translated dataframe to a new Excel file
df.to_excel("C:/Users/anind/Downloads/translated_file.xlsx", index=False)
