import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'Mukha_Dataset'

def getImageWithID(path):
	imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
	faces = []
	IDs = []
	for imagePath in imagePaths:
		faceImg = Image.open(imagePath).convert('L')
		faceNP = np.array(faceImg, "uint8")
		ID = int(os.path.split(imagePath)[-1].split('.')[1])
		faces.append(faceNP)
		IDs.append(ID)
		cv2.imshow("Nag-eensayoooo...", faceNP)
		cv2.waitKey(10)

	return IDs, faces

IDs, faces = getImageWithID(path)
recognizer.train(faces,np.array(IDs))
recognizer.save("train_data.yml")
cv2.destroyAllWindows()