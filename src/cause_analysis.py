import pandas as pd
import kaggle
import os

# Set up the path where we want to save the data
data_dir = "../data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Download the dataset using kaggle API
try:
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files('ivanchvez/causes-of-death-our-world-in-data', 
                                    path=data_dir, 
                                    unzip=True)
    print(f"Dataset downloaded to: {data_dir}")
    
    # List all files in the data directory
    all_files = os.listdir(data_dir)
    print(f"Files in directory: {all_files}")
    
    # Find the CSV file
    csv_files = [f for f in all_files if f.endswith('.csv')]
    if csv_files:
        csv_file = os.path.join(data_dir, csv_files[0])
        df = pd.read_csv(csv_file)
        
        # Print basic information about the dataset
        print("\nDataset Overview:")
        print("-----------------")
        print(f"Number of rows: {df.shape[0]}")
        print(f"Number of columns: {df.shape[1]}")
        print("\nColumns in the dataset:")
        print(df.columns.tolist())

        print("\nTime period covered:")
        print(f"From {df['Year'].min()} to {df['Year'].max()}")

        print("\nSample of unique countries:")
        print(df['Entity'].nunique(), "countries/regions in total")
        print(df['Entity'].unique()[:5], "... and more")

        print("\nFirst few rows of the dataset:")
        print(df.head())

        # Display basic statistical summary
        print("\nBasic statistical summary of numerical columns:")
        print(df.describe())
    else:
        print("No CSV files found in the data directory")
        
except Exception as e:
    print(f"An error occurred: {str(e)}")