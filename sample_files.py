import os
import random
import shutil
from tqdm import tqdm

def sample_files(folder_path):
    # List all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Calculate the number of files to sample (a quarter of the total files)
    num_files_to_sample = 1000
    
    # Randomly sample unique files
    sampled_files = random.sample(files, num_files_to_sample)
    
    # Create a subfolder named 'sampled_files' if it doesn't exist
    sampled_folder_path = os.path.join(folder_path, 'sampled_files_100')
    os.makedirs(sampled_folder_path, exist_ok=True)
    
    # Move the sampled files to the subfolder
    for file in tqdm(sampled_files):
        shutil.move(os.path.join(folder_path, file), os.path.join(sampled_folder_path, file))

# Example usage
folder_path = '/Users/user/Documents_stuff/Ashoka/monsoon24-courses/CV/code/final_project/data/kaggle-sat-seg/train/sampled_files_new'
sample_files(folder_path)


