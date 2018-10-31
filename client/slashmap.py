import boto3, requests
import time, json, logging
import settings

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

def getS3Key(s3_filename):
    return f"uncategorized/{s3_filename}"

def getS3Filename():
    return f"{time.time()}.jpg"

def uploadToS3(filepath, s3_filename):
    # Create an S3 client
    s3 = boto3.client('s3')
    # Uploads the given file using a managed uploader, which will split up large
    # files automatically and upload parts in parallel.
    s3.upload_file(filepath, settings.S3_BUCKETNAME, getS3Key(s3_filename))

def getAnalysis(s3_filename):
    try:
        r = requests.get(settings.API['analysis'], params={'s3key': getS3Key(s3_filename)})
        if r.status_code is 200: 
            labels = json.loads(r.content)
            return labels
        else:
            return []
    except Exception as e:
        logging.error(f"Error getting analysis: {e}")
        return []
