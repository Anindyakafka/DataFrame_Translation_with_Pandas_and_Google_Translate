# DataFrame Translation with Pandas and Google Translate

This project demonstrates how to translate the contents of a DataFrame using the `pandas` library and the `googletrans` library. The script reads an Excel file, translates its contents from Hindi to English, and saves the translated DataFrame to a new Excel file.

## Requirements

- Python 3.x
- `pandas` library
- `googletrans` library

## Installation

1. Install the required libraries using pip:

    ```sh
    pip install pandas googletrans
    ```

2. Ensure you have the input Excel file (`hindi.xlsx`) in the specified path.

## Usage

1. Place your input Excel file (`hindi.xlsx`) in the `C:/Users/anind/Downloads/` directory.

2. Run the script:

    ```sh
    python import_pandas_as_pd.py
    ```

3. The script will read the input file, translate its contents, and save the translated DataFrame to `translated_file.xlsx` in the same directory.

## Script Details

- The script reads the input Excel file using [pandas](http://_vscodecontentref_/0):

    ```python
    df = pd.read_excel("C:/Users/anind/Downloads/hindi.xlsx")
    ```

- It initializes the Google Translate API:

    ```python
    translator = Translator()
    ```

- The [batch_translate](http://_vscodecontentref_/1) function handles the translation in batches with error handling and retries:

    ```python
    def batch_translate(texts, src='hi', dest='en', batch_size=50, retries=3):
        # Function implementation
    ```

- The script translates each column in the DataFrame and creates new columns with English translations:

    ```python
    for column in df.columns:
        df[f'{column}_English'] = batch_translate(df[column].astype(str).tolist())
    ```

- Finally, it saves the translated DataFrame to a new Excel file:

    ```python
    df.to_excel("C:/Users/anind/Downloads/translated_file.xlsx", index=False)
    ```

## Example

Before translation:

| Column1 | Column2 |
|---------|---------|
| हिंदी    | नमस्ते  |
| भाषा    | दुनिया  |

After translation:

| Column1 | Column2 | Column1_English | Column2_English |
|---------|---------|-----------------|-----------------|
| हिंदी    | नमस्ते  | Hindi           | Hello           |
| भाषा    | दुनिया  | Language        | World           |

## License

This project is licensed under the MIT License.
