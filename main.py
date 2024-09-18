import cv2
import mediapipe as mp
import pyautogui
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(0)

def calculate_distance(point1, point2, frame_width, frame_height):
    x1, y1 = int(point1.x * frame_width), int(point1.y * frame_height)
    x2, y2 = int(point2.x * frame_width), int(point2.y * frame_height)
    distance = math.hypot(x2 - x1, y2 - y1)
    return distance

while True:
    success, frame = cap.read()
    if not success:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)
    frame_height, frame_width, _ = frame.shape

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            x = int(index_finger_tip.x * frame_width)
            y = int(index_finger_tip.y * frame_height)
            screen_x = int(index_finger_tip.x * screen_width)
            screen_y = int(index_finger_tip.y * screen_height)

            pyautogui.moveTo(screen_x, screen_y)
            cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)

            distance = calculate_distance(index_finger_tip, middle_finger_tip, frame_width, frame_height)

            # Eğer mesafe belli bir eşik değerden küçükse fare tıklasın (örn: 40 piksel)
            if distance < 40:
                pyautogui.click()

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Mouse Kontrolu", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
