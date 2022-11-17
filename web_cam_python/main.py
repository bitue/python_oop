import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap , QImage, QIcon
from PyQt5.QtCore import QTimer
import datetime 



class Main_Windows(QWidget):
    def __init__(self):
        super().__init__()
        # variable declare 
        self.window_height = 500 
        self.window_width = 700 
        # variable for image size 
        self.img_width = 700
        self.img_height = 500 
        # cap icon load 
        self.cam_icon = QIcon(cap_icon_path)
        self.rec_icon = QIcon(rec_icon_path)
        self.stop_icon = QIcon(stop_icon_path)
        
        #record flag 
        self.recording = False 

        #video 

        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')



       

        # set up the window 
        self.setWindowTitle("Bitue_web_cam")
        self.setGeometry(0,0, self.window_width, self.window_height)
        self.setFixedSize(self.window_width, self.window_height)
        #timer 
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.ui()


    
    def ui(self):
        self.image_level = QLabel(self)
        self.image_level.setGeometry(0,0, self.img_width, self.img_height)

        self.cap_btn = QPushButton(self)
        self.cap_btn.setIcon(self.cam_icon)
        self.cap_btn.setFixedSize(60, 60)
        self.cap_btn.clicked.connect(self.save_image)

        self.rec_btn = QPushButton(self)
        self.rec_btn.setIcon(self.rec_icon)
        self.rec_btn.setFixedSize(60, 60)
        self.rec_btn.clicked.connect(self.record)

        #layout setup 
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.cap_btn, 1,0)
        grid.addWidget(self.image_level, 0, 0)
        grid.addWidget(self.rec_btn, 2, 0)

        # if self.recording :
        #     self.rec_btn.setIcon(self.stop_icon)
       



        # ui te timer 
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
        
        self.show()

    def update(self):
        _, self.frame = self.cap.read()
        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        step = channel*width 
        q_frame = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        self.image_level.setPixmap(QPixmap.fromImage(q_frame))


    def save_image(self):
        print("Saving...........")
        self.get_time()
        cv2.imwrite(f"my_pic_{self.now_time}.png", self.frame)

    def record(self):
        if self.recording :
            print("Recording stop  ............")
            self.rec_btn.setIcon(self.rec_icon)
            
            self.recording = False
        else :
            print("Start recording .....")
            self.rec_btn.setIcon(self.stop_icon)
            self.get_time()

            self.out = cv2.VideoWriter(f"{self.now_time}.mp4", self.fourcc, 20.0 , (self.img_width, self.img_height))

          
            self.recording = True 
        
            

     

    def get_time(self):
        now = datetime.datetime.now()
        self.now_time = now.strftime("%y , %S") 


cap_icon_path = 'assets/photo.png'
rec_icon_path ='assets/video-camera (1).png'
stop_icon_path ='assets/stop-button.png'
app = QApplication(sys.argv)
win = Main_Windows()
sys.exit(app.exec_())




