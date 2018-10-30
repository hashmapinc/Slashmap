import json
import logging, os
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

S3_BUCKETNAME = os.environ['S3_BUCKETNAME']

def buildResponse(statusCode, body):
    return {
        "statusCode": statusCode,
        "headers": {
            'Access-Control-Allow-Origin': '*'
        },
        "body": json.dumps(body),
        "isBase64Encoded": True
    }

def handler(event, context):
    try:
        params = {'s3key': event['queryStringParameters']['s3key']}
        logging.info(f"sending request for {params['s3key']} to bucket {S3_BUCKETNAME}")
        rekognition = boto3.client('rekognition', region_name='us-east-1')
        response = rekognition.detect_labels(
            Image={
                "S3Object": {
                    "Bucket": S3_BUCKETNAME,
                    "Name": params['s3key'],
                }
            },
            MaxLabels=5,
            MinConfidence=90,
        )
        
        body = response['Labels']
        return buildResponse(200, body)

    except Exception as e:
        msg = f"error getting analysis: {e}"
        logger.error(msg)
        return buildResponse(500, msg)


    
