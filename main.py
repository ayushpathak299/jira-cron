import subprocess
import os

# Variables for the database connection
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Shell command to run the PostgreSQL function
command = f"PGPASSWORD={DB_PASSWORD} psql -h {DB_HOST} -p {DB_PORT} -U {DB_USER} -d {DB_NAME} -c 'SELECT transform_issue_data(false, 1);'"

# Run the command
subprocess.run(command, shell=True)
