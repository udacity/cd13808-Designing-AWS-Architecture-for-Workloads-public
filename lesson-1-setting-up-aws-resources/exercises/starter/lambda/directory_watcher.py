import os
import time

# Specify the directory to watch
WATCH_DIR = '/path/to/watch'

def watch_directory():
    print(f"Watching directory: {WATCH_DIR}")
    # Store the initial set of files
    initial_files = set(os.listdir(WATCH_DIR))

    while True:
        # Check the current set of files
        current_files = set(os.listdir(WATCH_DIR))
        # Determine if new files have been added
        new_files = current_files - initial_files
        if new_files:
            for file_name in new_files:
                print(f"New file uploaded: {file_name}")  # TODO: Replace with a notification email
            # Update the initial file set
            initial_files = current_files
        # Sleep for a short period before checking again
        time.sleep(5)

# Uncomment to run the local function
# watch_directory()