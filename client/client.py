import camera
import settings
import logging, time
import slashmap

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

def main():
    logger.info("STARTING CLIENT...")
    while True:
        time.sleep(30)

        logger.info("SNAPPING PICTURE...")
        camera.takePicture()
        logger.info(f"PICTURE SAVED TO {settings.IMG_PATH}...") 

        s3_filename = slashmap.getS3Filename()
        logger.info(f"Uploading to S3 {s3_filename}...")
        slashmap.uploadToS3(settings.IMG_PATH, s3_filename)
        logger.info(f"Getting analysis for {s3_filename}...")
        analysis = slashmap.getAnalysis(s3_filename)
        [print(f"label: {label['Name']}, conf: {label['Confidence']}") for label in analysis]


if __name__ == '__main__':
    main()
