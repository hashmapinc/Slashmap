import camera
import settings
import logging

logger = logging.getLogger(__name__)

def main():
    logger.info("STARTING CLIENT...")

    logger.info("SNAPPING PICTURE...")
    camera.takePicture()

    logger.info(f"PICTURE SAVED TO {settings.IMG_PATH}...") 

if __name__ == '__main__':
    main()
