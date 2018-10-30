# USAGE
# Start the server:
# 	app.py
# Submit a request via cURL:
# 	curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import flask
import io
from keras.models import load_model
import tensorflow as tf
import pandas as pd

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
model = load_model('ada_image_model.h5')
model._make_predict_function()
graph = tf.get_default_graph()

def prepare_image(image, target):
	# if the image mode is not RGB, convert it
	if image.mode != "RGB":
		image = image.convert("RGB")

	# resize the input image and preprocess it
	image = image.resize(target)
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)
	image = imagenet_utils.preprocess_input(image)

	# return the processed image
	return image

@app.route("/predict", methods=["POST"])
def predict():

	# ensure an image was properly uploaded to our endpoint
	if flask.request.method == "POST":
		if flask.request.files.get("image"):
			# read the image in PIL format
			image = flask.request.files["image"].read()
			image = Image.open(io.BytesIO(image))

			# preprocess the image and prepare it for classification
			image = prepare_image(image, target=(64, 64))
			#needed for Tensrflow
			global graph
			with graph.as_default():
				results = model.predict(image)
			#Simple check of the array value returned for assingment to predictions var	
				if results[0][0] == 0:
				    prediction = 'wheelchair'
				else:
				    prediction = 'not wheelchair'
	return flask.jsonify(prediction)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
	print(("* Loading Keras model and Flask starting server..."
		"please wait until server has fully started"))
	load_model('ada_image_model.h5')
	app.run()