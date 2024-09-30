import cv2
import mediapipe as mp
import time
from Finger import Finger
from interpretation import interpret

def add_space(text):
    return text + " "

def delete(text):
    return text[:-1]

def clear(text):
    return ""

def main():

    # Finger objects
    THUMB = Finger()
    INDEX = Finger()
    MIDDLE = Finger()
    RING = Finger()
    PINKY = Finger()

    # captures video from webcam
    # NOTE: input value can vary between -1, 0, 1, 2 (differs per device, 0 or 1 is common)
    # WARNING: VideoCapture does not work if another application is using camera (ie. video calling)
    cap = cv2.VideoCapture(0)

    # from pre-trained Mediapipe to draw hand landmarks and connections
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(max_num_hands=1)
    mpDraw = mp.solutions.drawing_utils

    # used to calculate FPS
    # pTime = 0  # previous time
    # cTime = 0  # current time

    # used to record letter every 3 seconds hand is in frame
    prev_time = time.time()
    curr_time = time.time()

    letters = ""

    while True:
        # reads image from webcam
        _, img = cap.read()
        h, w, c = img.shape                 # get height, width, depth

        # converts default image value to RGB value
        # NOTE: when printing back to the screen, use default value (img) NOT imgRGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB.flags.writeable = False  # improves performance
        # use Mediapipe to process converted RGB value
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:

            for handLms in results.multi_hand_landmarks:
                # creates list of all landmarks for easier indexing
                # list will have 21 values -> lm_list[0] will be first landmark
                lm_list = []

                # id corresponds to landmark #
                #   -> 21 landmarks in total (4 on non-thumb fingers, rest on thumb and palm)
                # lm corresponds to landmark value
                #   -> each lm has x coordinate and y coordinate
                #   -> default values are in ratio (value between 0 and 1)
                #   -> to convert to pixel value, multiple by width and height of screen
                for id, lm in enumerate(handLms.landmark):
                    # convert to x, y pixel values
                    cx, cy, cz = int(lm.x*w), int(lm.y*h), lm.z*c

                    lm_list.append([id, cx, cy, cz])

                # writes text to screen
                cv2.putText(img, str(interpret(lm_list)), (w-300, 70), cv2.FONT_HERSHEY_DUPLEX, 3, (52, 195, 235), 3)

                # draw hand landmarks and connections
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

                # countdown timer
                curr_time = time.time()
                diff_time = curr_time - prev_time
                if diff_time < 1:
                    display_time = 3
                elif diff_time < 2:
                    display_time = 2
                elif diff_time <= 3:
                    display_time = 1
                cv2.putText(img, str(display_time), (10,70), cv2.FONT_HERSHEY_DUPLEX, 3, (0,0,255), 3)
        else:
            # reset timer when hand not in frame
            prev_time = time.time()
        
        # capture letter of hand every three seconds
        curr_time = time.time()
        if curr_time - prev_time > 3:
            try:
                letters += interpret(lm_list)
            except TypeError:
                pass
            cv2.putText(img, "captured", (w//2 - 200,h//2), cv2.FONT_HERSHEY_DUPLEX, 3, (235, 107, 52), 3)
            prev_time = time.time()
        
        cv2.putText(img, letters, (10, h - 50), cv2.FONT_HERSHEY_DUPLEX, 3, (235, 143, 52), 3)

        
        # print FPS on screen (not console)
        # cTime = time.time()
        # fps = 1/(cTime-pTime)
        # pTime = cTime
        # cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3)

        # print current image captured from webcam
        cv2.imshow("Image", img)
        key = cv2.waitKey(1)

        # press Q to quit or "stop" button
        if key == ord("q"):
            break

    # cleanup
    cap.release()
    cv2.destroyAllWindows()


main()
