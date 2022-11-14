import cv2
import os 
from pathlib import Path


cam = cv2.VideoCapture(0)

count=0
while True:
	ret, frame = cam.read()

	cv2.imshow('frame', frame)

	# cek apakah folder savePerFrame ada
	if Path('savePerFrame').exists(): 
		# jika ada
		# cv2.imwrite('filename', frame)
		cv2.imwrite('E:\\pemrograman\\python\\2022\\open_cv\\project\\savePerFrame\\coba%d.jpg' % count, frame)
		if cv2.waitKey(60) == 27:
			break
		count+=1
	else:
		# jika tidak
		os.mkdir('SavePerFrame')


cam.release()
cv2.destroyAllWindows()
