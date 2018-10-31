import camera
import settings
import logging, time
import slashmap

def printAnalysis(analysis):
    print("\n\n")
    [print(f"label: {label['Name']}, conf: {label['Confidence']}") for label in analysis]
    print("\n\n")

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("STARTING CLIENT...")

    # loop
    while True:
        camera.takePicture()

        s3_filename = slashmap.getS3Filename()
        slashmap.uploadToS3(settings.IMG_PATH, s3_filename)
        logging.info(f"Getting analysis for {s3_filename}")
        analysis = slashmap.getAnalysis(s3_filename)
        printAnalysis(analysis)

        time.sleep(settings.LOOP_TIMEOUT)


if __name__ == '__main__':
    main()
