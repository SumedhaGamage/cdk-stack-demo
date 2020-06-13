import boto3
import os
import json
import base64

s3 = boto3.client('s3')
# dynmo_db = boto3.resource()

sizes = [(120, 120), (720, 720), (1600, 1600)]

def thubmnail_maker(event, context):

    bucket_name = os.environ.get('BUCKET_NAME')
    # table_name = os.environ.get('TABLE_NAME')
    data = event['body']
    dec = base64.b64decode(data)

    response = s3.put_object(
        ACL='public-read',
        Body=dec,
        Bucket=bucket_name,
        Key="myq.png"
        )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': "Content-Type",
            'Access-Control-Allow-Origin': 'http://localhost:4200',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(response)
    }
    