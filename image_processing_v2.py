import sys
import os
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class VideoProcessingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.video_capture = cv2.VideoCapture(0)  # Open webcam
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Video Processing App')
        layout = QVBoxLayout()
        self.label = QLabel(self)
        layout.addWidget(self.label)

        start_button = QPushButton('Start', self)
        start_button.clicked.connect(self.start_video_stream)
        layout.addWidget(start_button)

        stop_button = QPushButton('Stop', self)
        stop_button.clicked.connect(self.stop_video_stream)
        layout.addWidget(stop_button)

        save_button = QPushButton('Save Frame', self)
        save_button.clicked.connect(self.save_frame())
        layout.addWidget(save_button)

        self.setLayout(layout)

    def start_video_stream(self):
        while True:
            ret, frame = self.video_capture.read()
            if not ret:
                break
            # Perform image processing operations here
            # Display processed frame in the label

    def stop_video_stream(self):
        self.video_capture.release()

    # def save_frame(self):
    #     # Save the current processed frame as an image
    #     cv2.imwrite('processed_frame.jpg', processed_frame)
        
    
def save_frame(video_path, frame_num, result_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return
    
    os.makedirs(os.path.dirname(result_path), exist_ok=True)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
    ret, frame = cap.read()
    
    if ret:
        cv2.imwrite(result_path, frame)

def save_frame_range(video_path, start_frame, stop_frame, step_frame, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return
    
    os.makedirs(dir_path, exist_ok=True)
    
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(os.path.join(dir_path, f"{basename}_{start_frame}.{ext}"), frame)
            start_frame += step_frame
        else:
            break



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VideoProcessingApp()
    window.show()
    sys.exit(app.exec_())