import os
import time
### TODO: Import boto3 library 


### TODO: Configure SNS

## TODO: Comment out
WATCH_DIR = '/path/to/watch'

### TODO: Create the Lambda Handler
def watch_directory():

    ### TODO: Extract bucket name and object key from the event
    print(f"Watching directory: {WATCH_DIR}")
    initial_files = set(os.listdir(WATCH_DIR))

    ### TODO: Modify to send an SNS notification
    while True:
        current_files = set(os.listdir(WATCH_DIR))
        new_files = current_files - initial_files
        if new_files:
            for file_name in new_files:
                print(f"New file uploaded: {file_name}")  # TODO: Replace with a notification
            initial_files = current_files
        time.sleep(5)

    ### TODO: Add Return with status code and text
# watch_directory()