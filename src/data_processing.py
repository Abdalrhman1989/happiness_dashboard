import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
        return None

def clean_data_func(data):
    # Ensure necessary columns are present
    required_columns = {'Country', 'Score', 'Year'}
    if not required_columns.issubset(data.columns):
        missing = required_columns - set(data.columns)
        print(f"Error: Missing columns: {', '.join(missing)}")
        return None
    # Drop rows with missing values in required columns
    data = data.dropna(subset=required_columns)
    print("Data cleaned successfully.")
    return data
