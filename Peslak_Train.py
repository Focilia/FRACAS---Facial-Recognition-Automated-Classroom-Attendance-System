import os
import cv2
import numpy as np# Eto magconvert sa integer(uint8) para mabasa ng recognizer
from PIL import Image#Image Manipulation library sya para sa pag read ng face images

recognizer = cv2.face.LBPHFaceRecognizer_create()#Built in recognizer ng opencv LBPH algo sya
path = 'Mukha_Dataset'#path ng images ng faces

def getImageWithID(path):#Function para makuha image at id na nakalagay sa pangalan ng image
	imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
	faces = []#Empty dictionary para sa faces
	IDs = []#Empty dictionary para sa faces
	for imagePath in imagePaths:#for loop hanngang ma read lahat ng images
		faceImg = Image.open(imagePath).convert('L')#Mag convert sa grayscale incase na di naka gray image
		faceNP = np.array(faceImg, "uint8")#Gawin 8bit int yung images
		ID = int(os.path.split(imagePath)[-1].split('.')[1])#Para makuha ID num na nakalagay sa name ng image
		faces.append(faceNP)#Append para malagay sa list dun sa empty na dictionary sa taas
		IDs.append(ID)#Append para malagay sa list dun sa empty na dictionary sa taas
		cv2.imshow("Nag-eensayoooo...", faceNP)#Pangalang ng win
		cv2.waitKey(10)

	return IDs, faces

IDs, faces = getImageWithID(path)
recognizer.train(faces,np.array(IDs))#Kailangan para ma train recognizer at gawin nnyang data(yml extension sya)
recognizer.save("train_data.yml")#Eto yung trained data na ireread ng recognizer
cv2.destroyAllWindows()