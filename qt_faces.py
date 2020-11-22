from PIL import Image
import face_recognition
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer, qVersion
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit
import cv2
import os.path
import numpy as nd
from PIL import Image, ImageQt


def path():
    fname = QFileDialog.getOpenFileName(window, 'Open Image', 'D:\\Python_examples\\QT_faces_recognition\\faces',
                                        'Image files (*.jpg *.gif *.png)')
    imagePath = fname[0]
    print(fname[0])
    return imagePath


# LOAD IMAGE
def getImage():
    fname2 = path()

    # window.labelText.setText("Loading Image")
    pixmap = QPixmap(fname2)

    window.lb_images.setPixmap(QPixmap(pixmap))
    window.lb_images.setScaledContents(True)

    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file(fname2)

    face_locations = face_recognition.face_locations(image)

    print("I found {} face(s).".format(len(face_locations)))
    window.lb_qty.setText(format(len(face_locations)))

    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom,right))

        # You can access the actual face itself like this:
        global face_image
        face_image = image[top:bottom, left:right]

        # blur(face_image)
        pil_image = Image.fromarray(face_image)
        x = pil_image.toqpixmap()

        pixmap2 = QPixmap(x)
        window.lb_face.setPixmap(QPixmap(pixmap2))
        window.lb_face.setScaledContents(True)

    #if window.bt_blur2.isChecked():
        #print("Entrei")

        #img_blur = face_image
        # Blur the face image
        #face_image = cv2.GaussianBlur(img_blur, (99, 99), 30)

        #pil_image = Image.fromarray(face_image)
        #x = pil_image.toqpixmap()

        #pixmap2 = QPixmap(x)
        #window.lb_face.setPixmap(QPixmap(pixmap2))
        #window.lb_face.setScaledContents(True)


def blur():
    # img_blur = getImage()
    # Blur the face image
    # face_image = cv2.GaussianBlur(img_blur, (99, 99), 30)

    # pil_image = Image.fromarray(face_image)
    # x = pil_image.toqpixmap()

    # pixmap2 = QPixmap(x)
    # window.lb_face.setPixmap(QPixmap(pixmap2))
    # window.lb_face.setScaledContents(True)
    if window.bt_blur2.isChecked():
        print("Entrei")
        img_blur = face_image
        # Blur the face image
        face_image = cv2.GaussianBlur(img_blur, (99, 99), 30)

        pil_image = Image.fromarray(face_image)
        x = pil_image.toqpixmap()

        pixmap2 = QPixmap(x)
        window.lb_face.setPixmap(QPixmap(pixmap2))
        window.lb_face.setScaledContents(True)


def pil2pixmap(self, im):
    im = ImageQt.ImageQt(im)
    return window.QPixmap.fromImage(im)


app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("qt_face.ui")
window.bt_image.clicked.connect(getImage)
window.bt_blur.clicked.connect(blur)
# window.bt_load_image.clicked.connect(getImage)
# window.bt_threshold.clicked.connect(saveFileAs)
# window.labelFrameInput.setScaledContents(False)

# window.labelFrameOutput.setScaledContents(True)

# qtimerFrame = QTimer()
# qtimerFrame.timeout.connect(grabFrame)

window.show()
app.exec()
