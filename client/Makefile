all: run 

# install requirements
install:
	python3 -m pipenv install;

# get venv-activated python shell
shell:
	python3 -m pipenv run python;

# run the client
run: 
	python3 -m pipenv run python ./client.py;

# show the camera on the pi hdmi out
show: 
	raspistill -t 0;
