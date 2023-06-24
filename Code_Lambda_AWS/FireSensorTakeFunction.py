import json
import boto3
import calendar
from datetime import datetime
import time

# Create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')

# Use the DynamoDB object to select our tables
table_fire = dynamodb.Table('FireSensorTable')

# Define the handler function that the Lambda service will use
def lambda_handler(event, context):
 # Generate a timestamp for the event
    time_now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    current_GMT = time.gmtime()
    timestamp = calendar.timegm(current_GMT)

    # Write payload and time to the DynamoDB table using the object we instantiated and save response in a variable
    response = table_fire.put_item(
    Item={
        'Timestamp': timestamp,
        'Datetime': event['Datetime'],
        'Flame': event['Flame'],
        'CO': event['CO'],
        'Temp': event['Temp']

    })

    return {
       'statusCode': 200
    }
