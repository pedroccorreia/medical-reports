# Load environment dependent variables from yaml file
import yaml

with open('config.yaml', 'r') as file:
    config_info = yaml.safe_load(file)

PROJECT_NUMBER = config_info['project']['project_number']
PROJECT_ID = config_info['project']['project_id']
LOCATION= config_info['project']['location']


INPUT_BUCKET = config_info['storage']['input_bucket']


FIRESTORE_DATABASE = config_info['db']

SERVICE_ACCOUNT_KEY_FILE = 'secrets/credentials.json'
