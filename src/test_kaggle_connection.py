import kagglehub
import os

def test_kaggle_connection():
    print("Testing Kaggle Hub Connection")
    print("-" * 30)
    
    # Print kagglehub version
    print(f"Kagglehub version: {kagglehub.__version__}")
    
    try:
        # Attempt to download
        print("\nAttempting to download dataset...")
        path = kagglehub.dataset_download("ivanchvez/causes-of-death-our-world-in-data")
        
        print(f"\nDownload path returned: {path}")
        
        # Check if path exists
        if path and os.path.exists(path[0]):
            print(f"Directory exists: {path[0]}")
            
            # List contents of directory
            contents = os.listdir(path[0])
            print(f"\nContents of directory:")
            for item in contents:
                print(f"- {item}")
        else:
            print(f"Directory does not exist: {path[0]}")
            
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        print(f"Error type: {type(e)}")

if __name__ == "__main__":
    test_kaggle_connection() 