import cv2
import numpy as np
from flask import Flask, request, Response

app = Flask(__name__)


def acces_webcam():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('webcam', frame)
        if cv2.waitKey(1) == ord('q'):
                 break
        cap.release()
        cv2.destroyAllWindows()



@app.route('/')
def index():  # put application's code here
    return 'Bienvenue!'


if __name__ == '__main__':
    app.run()
