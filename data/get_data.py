import kagglehub
import shutil
import os

def download_energy_data():
    """
    Downloads the Energy Consumption dataset from Kaggle and saves the CSV 
    directly to the current folder.
    """
    handle = "nicholasjhana/energy-consumption-generation-prices-and-weather"
    file_name = "energy_dataset.csv"
    
    print(f"--- Downloading {file_name} from Kaggle ---")
    
    try:
        # Download the entire dataset (returns the path to the cached folder)
        path = kagglehub.dataset_download(handle)
        source_file = os.path.join(path, file_name)
        
        # Define destination (current folder)
        dest_file = os.path.join(os.path.dirname(__file__), file_name)
        
        # Copy the file to the local directory
        shutil.copy(source_file, dest_file)
        print(f"Successfully downloaded and saved to: {dest_file}")
        
    except Exception as e:
        print(f"Error downloading dataset: {e}")

if __name__ == "__main__":
    download_energy_data()
