
import boto3
import os
import json
from botocore.exceptions import ClientError

AWS_SECRET_KEY_ID = os.getenv('AWS_SECRET_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
DEFAULT_AWS_REGION = "us-west-1"
REPLICATE_KEY_PATH = "protea/replicate_api_token"

# Create a Secrets Manager client
session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=DEFAULT_AWS_REGION,
    aws_access_key_id=AWS_SECRET_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def get_secret(client, secret_name):
    try:
        # Get the secret value
        response = client.get_secret_value(SecretId=secret_name)

        # For secrets stored as a JSON string
        secret_string = response['SecretString']
        secret_dict = json.loads(secret_string)
        return secret_dict

    except ClientError as e:
        # Handle exceptions
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print(f"The secret with name '{secret_name}' was not found.")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print(f"Invalid request for the secret with name '{secret_name}'.")
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print(f"Invalid parameter for the secret with name '{secret_name}'.")
        else:
            print(f"Error retrieving secret with name '{secret_name}': {e}")

def set_replicate_api_token():
    if os.getenv('REPLICATE_API_TOKEN'):
        return
    else:
        secret_value = get_secret(client, REPLICATE_KEY_PATH)['protea/replicate_api_token']
        os.system(f'export REPLICATE_API_TOKEN="{secret_value}"')
        print(secret_value)

if __name__ == "__main__":
    set_replicate_api_token()
    print(os.getenv('REPLICATE_API_TOKEN'))