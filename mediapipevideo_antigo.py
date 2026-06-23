import cv2
import mediapipe as mp



mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture('video_para_testar_mediapipe.mp4')

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        
        cv2.imshow('MediaPipe', image)
        cv2.imshow('Original', frame)


        try:
            landmarks = results.pose_landmarks.landmark
            x_pose = landmarks[mp_pose.PoseLandmark.NOSE.value].x
            y_pose = landmarks[mp_pose.PoseLandmark.NOSE.value].y
            print(x_pose,y_pose)

        except:
            pass



        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

