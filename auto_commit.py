import os
import random
import time
from datetime import datetime

# Configuration
TOTAL_COMMITS = random.randint(1, 5) # Number of commits to make per run
FILE_NAME = "activity_log.txt"

def make_random_commit():
    for i in range(TOTAL_COMMITS):
        # Generate a random hex string or text change
        random_hex = os.urandom(8).hex()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Write the random data to a file
        with open(FILE_NAME, "a") as f:
            f.write(f"Update [{timestamp}]: Hex key {random_hex}\n")
        
        # Execute Git operations
        os.system(f"git add {FILE_NAME}")
        os.system(f'git commit -m "chore: automated test update {random_hex}"')
        
        print(f"Successfully generated commit {i+1}/{TOTAL_COMMITS}")
        time.sleep(1) # Short delay between commits

if __name__ == "__main__":
    # Ensure it's a git repo
    if not os.path.exists(".git"):
        os.system("git init")
    make_random_commit()
