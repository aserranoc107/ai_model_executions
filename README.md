# ai_model_executions
API to collect AI LLMs executions for audit
- You need to install boto3 and dotenv libraries in your local project
- AWS needs to be configure locally with access keys, please, consider this before trying to run the project
  - The best way to do this is to create an user with least rights and use its keys
- You also need to install the Python dependencies locally if you want to run it in your own environment
- Remember the correct ZIP, this is essential! 
- Feel free to text me if you need any help :) 


----.env

DB_PORT=5432 <PG usually uses this port. Make sure your Security Groups are well set!>
DB_SERVER_USER=dev_users
DB_HOST=<paste your DB host right here :) >
DB_NAME=<paste your DB name right here :)>
REGION=us-east-1 <make sure and double check your region!>
