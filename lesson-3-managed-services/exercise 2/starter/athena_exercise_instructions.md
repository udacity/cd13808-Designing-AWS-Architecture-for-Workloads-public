# Environment Setup 
- In the course repo, a CloudFormation file has been provided for you (athena-excercise-setup.yaml).
- This CloudFormation file will create an S3 bucket and populate it with data that you will analyze with Amazon Athena.
- The dataset is an opensource dataset from Kaggle. 
- As such, to successfully complete this exercise, you will need to do the following:
    - Sign up for a free Kaggle account here (or log in if you already have an account): https://www.kaggle.com/
    - Retrieve your Kaggle API key here: https://www.kaggle.com/me/account
    - If you this is your first time creating an API Key, (or you need to create a new API key):
        - Press "Create New Token" on the next screen.
        - Download the resulting file  
        - This will include your username and API key

- Once you have completed these steps, you can proceed to run the Cloudformation script:
    - Upload the Cloudformation script to your Cloud9 IDE
    - Add your Kaggle username and API key to the athena_exercise_setup_params.yaml file where specified.
    - Open the Cloud9 terminal and run the following command:
        - `aws cloudformation create-stack --stack-name athena-exercise-setup --template-body file://athena-exercise-setup.yaml --parameters file://athena_exercise_setup_params.json --capabilities CAPABILITY_NAMED_IAM`

# High Level Exercise Instructions
1. Configure your source and output folders in Athena to use the input and output buckets created by the Cloudformation script
2. Create your database: `CREATE DATABASE movies`
3. Run the provided query, using the demo for guidance when necessary. 