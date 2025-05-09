import json
import boto3
import os
from botocore.exceptions import ClientError

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('DYNAMODB_TABLE')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Parse the incoming event
        data = json.loads(event['body'])
        
        # Example: Assuming the data contains 'id' and 'value'
        item = {
            'id': data['id'],
            'value': data['value']
        }
        
        # Write the item to the DynamoDB table
        table.put_item(Item=item)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Data inserted successfully!'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }