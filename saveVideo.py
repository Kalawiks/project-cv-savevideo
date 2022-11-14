import cv2
import os
from pathlib import Path

cam = cv2.VideoCapture(0)

# mengambil width, height, and fps
width = int(cam.get(3))
height = int(cam.get(4))
fps = int(cam.get(5))
print(fps)

faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

# cek apakah folder vidRecord ada
if Path('vidRecord').exists():
	# jika ada kita akan pass
	pass
else:
	# jika tidak kita akan buat 
	os.mkdir('vidRecord')

def videoWrite(count):
	# cv2.VideoWriter(namafile, fourcc, fps, (column, row)) -> pada videowrite bertukar (row, column) menjadi (column, row)
	result = cv2.VideoWriter(f'E:\\pemrograman\\python\\2022\\open_cv\\project\\vidRecord\\filevid{count}.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))
		

	while True:
		ret, frame = cam.read()

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		face = faces.detectMultiScale(gray, 1.3, 5)
		for(x, y, w, h) in face:
			cv2.rectangle(frame, (x, y), (x+w, y+h), [0, 255, 0], 3)

		result.write(frame)

		cv2.imshow('frame', frame)
		if cv2.waitKey(1) == ord('q'):
			break
		elif cv2.waitKey(1) == ord('s'):
			cv2.imwrite(f'Screenshots.jpg', frame)
			print('Frame Captured!!!')

	cam.release()
	result.release()
	cv2.destroyAllWindows()

count = 1

while True:
	if not(os.path.isfile(f'E:\\pemrograman\\python\\2022\\open_cv\\project\\vidRecord\\filevid{count}.avi')):
		videoWrite(count)
		break
	else:
		count+=1

