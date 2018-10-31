import camera
import settings
import logging, time
import slashmap

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("STARTING CLIENT...")

    # loop
    while True:
        try:
            camera.takePicture()

            s3_filename = slashmap.getS3Filename()
            slashmap.uploadToS3(settings.IMG_PATH, s3_filename)
            logging.info(f"Getting analysis for {s3_filename}")
            analysis = slashmap.getAnalysis(s3_filename)
            print("\n")
            slashmap.validate(analysis)
            print("\n")

        except Exception as e:
            logging.error(f"Error in main loop: {e}")
        
        time.sleep(settings.LOOP_TIMEOUT)


if __name__ == '__main__':
    main()
