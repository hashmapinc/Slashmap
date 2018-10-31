LOOP_TIMEOUT = 5 # num seconds between sending pics
IMG_PATH='image.jpg'
S3_BUCKETNAME='slashmap-images'
url = 'https://hah5b9rfgi.execute-api.us-east-1.amazonaws.com/dev'
API = {
    'analysis': f"{url}/analysis",
}
VIOLATION_MSG = "VIOLATION"
OK_MSG = "ALL CLEAR"
DEEP_LEARNING_URL = "http://ec2-52-15-109-73.us-east-2.compute.amazonaws.com:5000/predict"
MATCHING_LABELS = set(["CAR", "CARS", "LICENSE", "LICENSE PLATE", "TRUCK", "AUTO", "AUTOMOBILE", "AUTOMOBILES", "TRANSPORTATION", "VEHICLE", "CAR MIRROR", "CAR MIRRORS", "VEHICLES", "TRUCKS"])