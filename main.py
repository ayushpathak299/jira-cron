import subprocess

# Variables for the database connection
DB_HOST = "jira-redash.c5ditj8vhg0k.us-west-1.rds.amazonaws.com"
DB_PORT = "5432"
DB_NAME = "jira"
DB_USER = "redash"
DB_PASSWORD = "N6ZrFz8KdR"

# Shell command to run the PostgreSQL function
command = f"PGPASSWORD={DB_PASSWORD} psql -h {DB_HOST} -p {DB_PORT} -U {DB_USER} -d {DB_NAME} -c 'SELECT transform_issue_data(false, 1);'"

# Run the command
subprocess.run(command, shell=True)
