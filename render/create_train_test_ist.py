import os
import random
import time

# Directory containing the files
dir_path = './output/thingi10k_depth_fixed8/'

# Get a list of all files in the directory
all_files = os.listdir(dir_path)

# Calculate 80% of the total number of files
num_files = int(len(all_files) * 0.8)
# Randomly select 80% of the files for the training list
train_files = random.sample(all_files, num_files)

# Subtract the training files from the total files to get the test files
test_files = list(set(all_files) - set(train_files))

# Remove file extensions
train_files = [os.path.splitext(file)[0] for file in train_files]
test_files = [os.path.splitext(file)[0] for file in test_files]

# Create the training list file
with open('thingi10k_train.list', 'w') as f:
    for file in train_files:
        f.write(f'thingi10k/{file}\n')

# Create the test list file
with open('thingi10k_test.list', 'w') as f:
    for file in test_files:
        f.write(f'thingi10k/{file}\n')