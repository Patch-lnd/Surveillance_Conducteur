import cv2
import dlib
import imutils
import numpy as np
from imutils import face_utils
from scipy.spatial import distance as dist
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow(winname:"Camera", frame)

    gray = cv2.cvtColor(frame,cv2.CLOR_BGR2GRAY)
    face= detector(gray, 1)
    for face in face:
        landmarks = predictor(gray,face)
        landmarks_np =face_utils.shape_to_np(landmarks)
        for(x,y) in landmarks_np:
            cv2.circle(frame, center: (x,y), raduis: 2, color: (0,255,0), -1)
        (x,y,w,h) = face_utils.rect_to_bb(face)
        cv2.imshow(winname: "dectection des landmarks -Dlib", frame)

        if cv2.waitkey(1) & 0xFF == ord('q'): 
            break

        def eye_aspect_ratio(eye_points): 
            vertical = np.linalg.norm(np.array(eye_points[1])- np.array(eye_points[5]))
            vertical2 = np.linalg.norm(np.array(eye_points[2])- np.array(eye_points[4]))
            horizontal = np.linalg.norm(np.array(eye_points[0])- np.array(eye_points[3]))
            ear = (2.0 * horizontal)/(vertical + vertical2)
            return ear
        left_eye = []
        right_eye = []
        for i in range(37,43):
            landmarks = predictor(gray, face)
            landmarks_np = face_utils.shape_to_np(landmarks)
            left_eye.append((landmarks.part(i).x, landmarks.part(i).y))

        for i in range(43,49):
            landmarks = predictor(gray, face)
            landmarks_np = face_utils.shape_to_np(landmarks)
            left_eye.append((landmarks.part(i).x, landmarks.part(i).y))

        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        avg_ear = (left_ear + right_ear)/ 2.0

        if avg_ear > 0.25:
            print("yeux ouvert")
        elif avg_ear < 0.25:
            print("yeux fermé")
        else:
            print("confus")
        print(f"valeur ear:{avg_ear}")
        cap.release()
        cv2.destroyAllWindows()
        print("Porgramme Terminé")
