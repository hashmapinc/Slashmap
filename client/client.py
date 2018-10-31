import camera
import settings
import logging, time
import slashmap

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("STARTING CLIENT...")

    # loop
    while True:
        logging.info("SNAPPING PICTURE...")
        camera.takePicture()
        logging.info(f"PICTURE SAVED TO {settings.IMG_PATH}...") 

        s3_filename = slashmap.getS3Filename()
        logging.info(f"Uploading to S3 {s3_filename}...")
        slashmap.uploadToS3(settings.IMG_PATH, s3_filename)
        logging.info(f"Getting analysis for {s3_filename}...")
        analysis = slashmap.getAnalysis(s3_filename)
        [print(f"label: {label['Name']}, conf: {label['Confidence']}") for label in analysis]

        time.sleep(settings.LOOP_TIMEOUT)


if __name__ == '__main__':
    main()
