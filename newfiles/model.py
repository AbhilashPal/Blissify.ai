import keras
from keras.models import model_from_json
import cv2
import os

model = model_from_json(open('model.json').read())
model.load_weights('weights.h5')


def predict(X):
	image = cv2.resize(X,(64,64), interpolation = cv2.INTER_CUBIC)
	image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	image = image.reshape(1,64,64,1)
	p = model.predict(image)
	p=p[0]
	print(p)
	for i in range(len(p)):
		if p[i]==max(p):
			if i == 3:
				return(1)
			else:
				return (0)