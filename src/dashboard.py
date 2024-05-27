import pandas as pd
import plotly.express as px
import os

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

def create_bar_chart(data):
    try:
        top10 = data.nlargest(10, 'Score')
        fig = px.bar(top10, x='Country', y='Score', color='Year', title='Top 10 Happiest Countries')
        return fig
    except KeyError as e:
        print(f"Error: {e}")
        return None

def create_dashboard(file_path):
    data = load_data(file_path)
    if data is None:
        return
    cleaned_data = clean_data_func(data)
    if cleaned_data is None:
        return
    figure = create_bar_chart(cleaned_data)
    if figure:
        figure.show()

if __name__ == "__main__":
    create_dashboard('../data/happiness.csv')
