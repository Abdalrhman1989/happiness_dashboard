import pandas as pd
import os

def inspect_data(file_path):
    """Load data from a CSV file and print its structure."""
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.\n")
        print("Data Head:\n", data.head(), "\n")
        print("Data Columns:\n", data.columns, "\n")
        return data
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, '../data/happiness.csv')
    data = inspect_data(data_path)
