import boto3
import os
import json
import base64
import random

s3 = boto3.client('s3')
table = boto3.client('dynamodb')

sizes = [(120, 120), (720, 720), (1600, 1600)]

def thubmnail_maker(event, context):

    bucket_name = os.environ.get('BUCKET_NAME')
    table_name = os.environ.get('TABLE_NAME')
    data = event['body']
    dec = base64.b64decode(data)
    key = "{}.png".format(random.randint(10, 100))
    response = "https://{}.s3.amazonaws.com/{}".format(bucket_name, key)

    s3.put_object(
        ACL='public-read',
        Body=dec,
        Bucket=bucket_name,
        Key=key
        )
    
    table.put_item(
        TableName=table_name,
        Item={
            "id": {'S': key},
            "url": {'S': response}
        }
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': "Content-Type",
            'Access-Control-Allow-Origin': 'http://localhost:4200',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps({"object_url":response})
    }
    