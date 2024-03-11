import sys
import os
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QSlider, QAction, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QTimer,QDateTime
from PyQt5.QtGui import QImage, QPixmap


class VideoProcessor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.video_source = 0  # Default to webcam
        self.cap = cv2.VideoCapture(self.video_source)

        self.frame_label = QLabel(self)
        self.frame_label.setAlignment(Qt.AlignCenter)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

        self.start_button = QPushButton("Start", self)
        self.start_button.setObjectName("startButton")
        self.start_button.clicked.connect(self.start_video)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setObjectName("stopButton")
        self.stop_button.clicked.connect(self.stop_video)

        self.threshold_slider = QSlider(Qt.Horizontal, self)
        self.threshold_slider.setMinimum(0)
        self.threshold_slider.setMaximum(255)
        self.threshold_slider.setValue(127)

        self.save_button = QPushButton("Save Frame", self)
        self.save_button.setObjectName("saveButton")
        self.save_button.clicked.connect(self.save_frame)

        self.open_file_action = QAction("Open Video File", self)
        self.open_file_action.setObjectName("openFileAction")
        self.open_file_action.triggered.connect(self.open_file)

        self.toolbar = self.addToolBar("Options")
        self.toolbar.addAction(self.open_file_action)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.frame_label)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.threshold_slider)
        self.layout.addWidget(self.save_button)
        self.layout.setContentsMargins(50, 50, 50, 50)
        self.layout.setSpacing(20)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.image_processor = self.gray_scale

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 10px 24px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                cursor: pointer;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QSlider {
                padding: 0 20px;
            }
        """)


    def start_video(self):
        self.timer.start(1000 // 30)  # 30 fps
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_video(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            processed_frame = self.image_processor(frame)
            self.display_frame(processed_frame)

    # def display_frame(self, frame):
    #     height, width, channel = frame.shape
    #     bytes_per_line = 3 * width
    #     q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
    #     pixmap = QPixmap.fromImage(q_img)
    #     self.frame_label.setPixmap(pixmap)
            
    def display_frame(self, frame):
        if len(frame.shape) == 3:  # Color image
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        else:  # Grayscale image
            height, width = frame.shape
            bytes_per_line = width
            q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

        pixmap = QPixmap.fromImage(q_img)
        self.frame_label.setPixmap(pixmap)


    def save_frame(self):
        ret, frame = self.cap.read()
        if ret:
            folder_path = QFileDialog.getExistingDirectory(self, "Select Directory to Save Frames")
            if folder_path:
                timestamp = QDateTime.currentDateTime().toString("yyyy-MM-dd_hh-mm-ss")
                filename = os.path.join(folder_path, f"processed_frame_{timestamp}.png")
                cv2.imwrite(filename, self.image_processor(frame))
                QMessageBox.information(self, "Information", "Frame saved successfully!")


    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4 *.avi)")
        if filename:
            self.cap.release()  # Release the previous capture
            self.cap = cv2.VideoCapture(filename)
            if not self.cap.isOpened():
                QMessageBox.critical(self, "Error", "Failed to open video file!")
            else:
                self.start_video()

    def update_threshold(self):
        threshold_value = self.threshold_slider.value()
        self.image_processor = lambda frame: self.edge_detection(frame, threshold_value)

    @staticmethod
    def gray_scale(frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def edge_detection(frame, threshold):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, threshold / 2, threshold)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VideoProcessor()
    window.setWindowTitle("Video Processor")
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec_())
