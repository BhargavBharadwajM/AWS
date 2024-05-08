import json
import boto3

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
# use the DynamoDB object to select our table
table = dynamodb.Table('leavereq')
def lambda_handler(event, context):
  try:
    # Debugging: Print the event object (optional)
    print("Event: ", event)

    # extract values from the event object
    id = event['body']['empid']
    startDate = event['body']['startDate']
    endDate = event['body']['endDate']

    # write data to the DynamoDB table
    response = table.put_item(
      Item={
        'empid': id,
        'startDate': startDate,
        'endDate': endDate
      })

    # prepare response with CORS headers
    headers = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Allow-Methods': 'POST,OPTIONS'
    }

    # return a prope…
[12:25, 4/19/2024] Bhargav M: # define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    try:
        # Debugging: Print the event object (optional)
        print("Event: ", event)

        # extract values from the event object
        request_body = json.loads(event['body'])
        id = request_body['empid']
        startDate = request_body['startDate']
        endDate = request_body['endDate']

        # write data to the DynamoDB table
        response = table.put_item(
            Item={
                'empid': id,
                'startDate': startDate,
                'endDate': endDate
            })

        # prepare response with CORS headers
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'POST,OPTIONS'
        }

        # return a properly formatted JSON object with CORS headers
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps('Leave request submitted successfully')  # Add a success message
        }

    except KeyError as e:
        # Handle KeyError
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'POST,OPTIONS'
        }
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps(f'Missing key: {e}')
        }

    except Exception as e:
        # Handle other exceptions
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'POST,OPTIONS'
        }
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps(f'Internal Server Error: {e}')
        }
