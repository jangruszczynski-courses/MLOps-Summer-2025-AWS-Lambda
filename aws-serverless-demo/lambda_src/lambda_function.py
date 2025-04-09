# We should be using loggers instead of print statements
# https://stackoverflow.com/questions/37703609/using-python-logging-with-aws-lambda

import boto3
from datetime import datetime

def lambda_handler(event, context):

    # Log input event and context
    print("Event: %s", event)
    print("Context: %s", context)
    print()
    # Save "Hello World" to S3
    s3_client = boto3.client('s3')
    bucket_name = 'my-test-bucket-xd'
    file_name = f"hello-world-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.txt"
    print("XD")
    s3_client = boto3.client('s3')
    # download from bucket
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body='Hello World'
        )
        print("Successfully saved to %s/%s", bucket_name, file_name)
    except Exception as e: # Too generic catch
        print("Error saving to S3: %s", e)
        raise
    
    return {
        'statusCode': 200,
        'body': f'Hello, World! Saved to {bucket_name}/{file_name}'
    }



if __name__ == "__main__":
    result = lambda_handler(None, None)
    print(f"Result: {result}")
