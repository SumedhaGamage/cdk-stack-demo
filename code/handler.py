import PIL.Image as Image
import boto3
import os

s3 = boto3.resource('s3')
# dynmo_db = boto3.resource()

sizes = [(120, 120), (720, 720), (1600, 1600)]

def tubmnail_maker(event, context):

    bucket_name = os.environ.get('BUCKET_NAME')
    # table_name = os.environ.get('TABLE_NAME')

    # for size in sizes:
        # image = Image.frombytes('L', (1600,1600), event.body)
        # image.thumbnail(size)
        # s3.Bucket(bucket_name).upload_fileobj()
        
    print(event)
    # print(context)
    return {
        'statusCode': 200,
        'body' : {
            'event': event
            # 'context': context
        }
    }
    