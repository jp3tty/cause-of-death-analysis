import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
import os

def load_and_analyze_data():
    try:
        print("Setting up data directory...")
        # Create data directory if it doesn't exist
        data_dir = os.path.join(os.getcwd(), '../data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            
        # print("Authenticating with Kaggle...")
        # Initialize the Kaggle API
        api = KaggleApi()
        api.authenticate()
        
        # print("Downloading dataset...")
        # Download the dataset
        api.dataset_download_files('ivanchvez/causes-of-death-our-world-in-data',
                                 path=data_dir,
                                 unzip=True)
        
        print(f"\nContents of data directory:")
        contents = os.listdir(data_dir)
        for item in contents:
            full_path = os.path.join(data_dir, item)
            size = os.path.getsize(full_path) / 1024  # Size in KB
            print(f"- {item} ({size:.2f} KB)")
            
        # Find CSV files
        csv_files = [f for f in contents if f.endswith('.csv')]
        if not csv_files:
            raise FileNotFoundError("No CSV files found in the downloaded dataset")
            
        # Read both CSV files
        dataframes = {}
        for csv_file in csv_files:
            csv_path = os.path.join(data_dir, csv_file)
            # print(f"\nAttempting to read: {csv_file}")
            df = pd.read_csv(csv_path)
            dataframes[csv_file] = df
            
            # Print basic information about each dataset
            print(f"\nDataset Overview for {csv_file}:")
            print("-" * (23 + len(csv_file)))
            print(f"Number of rows: {df.shape[0]}")
            print(f"Number of columns: {df.shape[1]}")
            # print("\nColumns in the dataset:")
            # print(df.columns.tolist())

            if 'Year' in df.columns:
                print("\nTime period covered:")
                print(f"From {df['Year'].min()} to {df['Year'].max()}")

            if 'Entity' in df.columns:
                print("\nSample of unique countries:")
                print(f"{df['Entity'].nunique()} countries/regions in total")
                print(f"Sample: {list(df['Entity'].unique()[:5])}")

            # print("\nFirst few rows of the dataset:")
            # print(df.head())

            # print("\nBasic statistical summary of numerical columns:")
            # print(df.describe())
            # print("\n" + "="*50 + "\n")  # Separator between datasets
        
        return dataframes
        
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        print(f"Error type: {type(e)}")
        return None

if __name__ == "__main__":
    dfs = load_and_analyze_data()
    if dfs:
        print("\nDatasets loaded successfully!")
        print("Available dataframes:", list(dfs.keys()))