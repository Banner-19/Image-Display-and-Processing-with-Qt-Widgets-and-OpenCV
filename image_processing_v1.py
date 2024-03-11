import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QSlider
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap


class VideoProcessor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.video_source = 0  # Default to webcam
        self.cap = cv2.VideoCapture(self.video_source)

        self.frame_label = QLabel(self)
        self.frame_label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.frame_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_video)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop_video)

        self.threshold_slider = QSlider(Qt.Horizontal, self)
        self.threshold_slider.setMinimum(0)
        self.threshold_slider.setMaximum(255)
        self.threshold_slider.setValue(127)
        self.threshold_slider.valueChanged.connect(self.update_threshold)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.threshold_slider)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.image_processor = self.gray_scale

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

    def display_frame(self, frame):
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(q_img)
        self.frame_label.setPixmap(pixmap)

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
