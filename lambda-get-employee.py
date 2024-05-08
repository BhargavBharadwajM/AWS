getEmployee.py
import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table('EmployeeProfile')

    try:
        response = table.scan()
        data = response['Items']

        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])

        # Prepare response with CORS headers
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST,OPTIONS'
        }

        # Return a properly formatted response
        return {
            'statusCode': 200,
            'headers': headers,  # Include CORS headers in every response
            'body': json.dumps(data)
        }
            
    except Exception as e:
        # Return an error response if an exception occurs, including CORS headers
        return {
            'statusCode': 500,
            'headers': headers,  # Include CORS headers even in error responses
            'body': json.dumps({'error': str(e)})
        }
