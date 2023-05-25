import subprocess
import os
import json


bigquery_credential = os.environ.get('BIGQUERY_CREDS')
directory_of_file = os.path.dirname(os.path.realpath(__file__))
dbt_command = os.environ.get('dbt_command', 'dbt run')

os.chdir(directory_of_file)
if not bigquery_credential or not bigquery_credential =='None':
    bigquery_credential = json.loads(bigquery_credential)
    with open('bigquery_creds.json', 'w') as outfile:
        json.dump(bigquery_credential, outfile)

subprocess.run('sh', '-c', dbt_command, check=True)