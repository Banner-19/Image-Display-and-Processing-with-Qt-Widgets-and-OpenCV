# Vyorius Drones Private Limited
Vyorius is a SaaS platform for mobile unmanned robots, providing direct plug and play while bringing all of the command, control, supervision, management, asset tracking and maintenance tools in one place. AI algorithms will utilize the data we gather for predictive maintenance and finding efficient vehicles in the fleet.

# Assignment
The project is a Python application built using the PyQt5 library for the graphical user interface (GUI) and OpenCV for video processing. Here's a detailed elaboration of the project:

# Purpose: 
The purpose of the project is to create a user-friendly application for capturing video from a webcam or a video file, processing the video frames in real-time using various image processing techniques, and providing options for users to control the video stream, adjust processing parameters, and save processed frames.

# Components:
* __GUI:__ The graphical user interface (GUI) is created using PyQt5, a popular Python library for building cross-platform desktop applications. The GUI consists of various widgets arranged in a window, including buttons, sliders, labels, and a toolbar.
* __Video Capture:__ The application captures video frames from a webcam by default or from a specified video file. It uses the OpenCV library to interact with video sources and capture frames.
* __Image Processing:__ The application provides basic image processing functionalities such as grayscale conversion and edge detection. These operations are applied to each frame of the video stream in real-time.
* __User Controls:__ The GUI includes buttons for starting and stopping the video stream, a slider for adjusting image processing parameters (e.g., threshold value for edge detection), and options for opening video files and saving processed frames.
* __Frame Display:__ The processed video frames are displayed in a QLabel widget within the GUI window. OpenCV is used to convert the processed frames into a format compatible with PyQt5 for display.
* __File Handling:__ Users can open video files using the toolbar option and save processed frames to a specified directory using the "Save Frame" button.

# Functionality:
* __Start/Stop Video Stream:__ Users can start and stop the video stream from the webcam or a video file using the "Start" and "Stop" buttons, respectively.
* __Adjust Parameters:__ Users can adjust image processing parameters (e.g., threshold value for edge detection) using the slider provided in the GUI.
* __Open Video Files:__ Users can select and open video files using the toolbar option to process and display video from the selected file.
* __Save Processed Frames:__ Users can save processed frames as PNG images to a specified directory using the "Save Frame" button. Each saved frame is timestamped for identification.

# Styling:
* The GUI elements are styled using CSS-like style sheets to enhance their appearance and provide a visually appealing user interface.
* Colors, padding, borders, and other properties are customized to create a cohesive and attractive design.

# Extensibility:
* The project can be extended to include additional image processing algorithms and user controls based on requirements.
* More complex image processing techniques such as object detection, face recognition, or feature tracking can be implemented and integrated into the application.
* Additional widgets, menus, or dialog boxes can be added to provide more functionalities and improve the user experience.

Overall, the project demonstrates the integration of PyQt5 and OpenCV to create a feature-rich desktop application for real-time video processing and manipulation. It serves as a foundation for building more advanced computer vision applications with a user-friendly interface.





