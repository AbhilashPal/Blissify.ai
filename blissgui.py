# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blissifydotai1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit
import sys
import numpy as np
import cv2
from textblob import TextBlob
import model
import urllib
import outputfile

class Ui_Form(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(881, 561)
        Form.setLayoutDirection(QtCore.Qt.RightToLeft)
        Form.setStyleSheet("background-color: rgb(17, 17, 17);\n"
"background-color: rgb(223, 223, 223);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(720, 180, 141, 71))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(370, 180, 301, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-image: url(:/aa/Blank.png);")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(370, 350, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-image: url(:/aa/Blank.png);")
        self.label_2.setObjectName("label_2")
        self.textBrowser =  QLineEdit(self)
        self.textBrowser.setGeometry(QtCore.QRect(370, 490, 321, 31))
        self.textBrowser.setStyleSheet("background-image: url(:/asv/Untitled.png);")
        self.textBrowser.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 350, 131, 61))
        self.pushButton_2.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 201, 151))
        self.label.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../../Users/Saurav/Desktop/b67e9782-4194-4cd7-af72-0e84e52dac64.png"))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 300, 271, 221))
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../../../../../Users/Saurav/Desktop/DKmSnb_V4AAt770asc.jpg"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(35, 120, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Blissify.ai"))
        Form.setWhatsThis(_translate("Form", "<html><head/><body><p><img src=\":/x/bliss.jpg\"/></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Let\'s click your photo"))
        self.label_3.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#000000;\">The first step is for you to let us </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#000000;\">know how you are feeling and we </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#000000;\">feel nothing is more expressive </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#000000;\">than your beautiful face</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt; color:#000000;\">If you think that you can express </span></p><p align=\"justify\"><span style=\" font-size:14pt; color:#000000;\">yourself better through words </span></p><p align=\"justify\"><span style=\" font-size:14pt; color:#000000;\">then you can let your heart out. </span></p><p align=\"justify\"><span style=\" font-size:14pt; color:#000000;\">Enter your thoughts in the dialog box</span></p><p align=\"justify\"><span style=\" font-size:14pt; color:#000000;\"><br/></span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "Let us know \n"
"about your \n"
"thoughts"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Your Friend for every mood :P</span></p></body></html>"))
        self.pushButton_2.clicked.connect(self.sentimental)
        self.pushButton.clicked.connect(self.haar)


    def sentimental(self):
        
        s=self.textBrowser.text()
        print(s)
        testimonial = TextBlob(s)
        #print(testimonial.sentiment.polarity)
        x=testimonial.sentiment.polarity
        x=x*50
        print(x)
        
        
    def haar(self):
        
        
        face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        
        cap=cv2.VideoCapture(0)
        
        while True:
            ret,frame=cap.read()
            
            frame1=frame
            cv2.imwrite("frame.jpeg",frame1)
            
            #cv2.imshow('frame1',frame1)
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces=face_cascade.detectMultiScale(gray,1.3,5)
            
 
            for(x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

                

                image=frame[y:y+h,x:x+w]
                image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                #cv2.imshow('Press v to click',image)
                image = cv2.resize(image,(200,200), interpolation = cv2.INTER_CUBIC)
        
        
                #roi_gray=gray[y:y+h,x:x+h]
                #roi_color=frame[y:y+h,x:x+h]
                '''
                eyes=eye_cascade.detectMultiScale(roi_gray)
                for(ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    '''
    
            cv2.imshow('Press v to click',frame)
            if cv2.waitKey(1) & 0xff==ord('v'):
                cv2.imwrite("face.jpg",image)
                break
            
        x=cv2.imread("face.jpg")
        
        #print(r.json())
        
        
        #print(r1.json())
        z=0
        import requests
        p=model.predict(x)
        print(p)
        
        if p==1:
            r = requests.post(
    "https://api.deepai.org/api/fast-style-transfer",
    files={
        'image': open('frame.jpeg', 'rb'),
        'style': 'rain-princess.ckpt',
    },
    headers={'api-key': 'e7b99044-d936-4112-8649-4bd0781ecbbe'}
)
            url=r.json()['output_url']
            print(url)

            full_file_name = 'elon_musk' + '.jpg'
            urllib.request.urlretrieve(url,full_file_name)
            print("x1")
        else:
            r = requests.post(
    "https://api.deepai.org/api/fast-style-transfer",
    files={
        'image': open('frame.jpeg', 'rb'),
        'style': 'scream.ckpt',
    },
    headers={'api-key': 'e7b99044-d936-4112-8649-4bd0781ecbbe'}
)
            url=r.json()['output_url']
            print(url)

            full_file_name = 'elon_musk' + '.jpg'
            urllib.request.urlretrieve(url,full_file_name)
            print("x0")
            
            
        
    

        

        cap.release()
        cv2.destroyAllWindows()
        x=50
        outputfile.getout(p,x)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Ui_Form()
    ex.show()
    sys.exit(app.exec())

