import json

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
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    return buildResponse(200, body)