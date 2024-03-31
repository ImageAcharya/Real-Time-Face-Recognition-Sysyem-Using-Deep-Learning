

import cv2
import numpy as np 
import matplotlib.pyplot as plt
import keras
from tensorflow.keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent


def facepredict(cropped):
  new_model = keras.models.load_model(BASE_DIR / 'saved_model_vgg_final.h5')
  dim = (224,224)
  cropped = cv2.resize(cropped, dim)

  X = image.img_to_array(cropped)
  X = np.expand_dims(X, axis=0)
  X = preprocess_input(X)

  value = new_model.predict(X)

  probas = np.array(value)
  labels = (probas > 0.5).astype(np.int)

  if labels[0][0]==1:
    return("Aarati Yadav")
  elif labels[0][1]==1:
    return("Aasish Khakural")
  elif labels[0][2]==1:
    return("Amit Baral")
  elif labels[0][3]==1:
    return("Asmit Aryal")
  elif labels[0][4]==1:
    return("Asmita Lamichhane")
  elif labels[0][5]==1:
    return("Dikshya Ghimire")
  elif labels[0][6]==1:
    return("Ganesh Baral")
  elif labels[0][7]==1:
    return("Image Acharya")
  elif labels[0][8]==1:
    return("Kamal Ghimire")
  elif labels[0][9]==1:
    return("Rupesh Aryal")
  elif labels[0][10]==1:
    return("Safal Panta")
  elif labels[0][11]==1:
    return("Sagar Panta")
  elif labels[0][12]==1:
    return("Sangam Acharya")
  elif labels[0][13]==1:
    return("Srijana Wagle")
  else:
    return("Sulav Shrestha")

