# REAL-TIME ATTENDANCE SYSTEM WITH FACE RECOGNITION

The most arduous task in any organization is attendance marking. To resolve this problem, 
smart and auto attendance management system is being utilized. The smart attendance 
system is generally executed with the help of biometrics. But authentication is an important 
prerequisite in this system. Face recognition is one of the biometric methods to improve this 
system. The main implementation steps used in this type of system are face detection and 
recognizing the detected face.

## Project Overview

This project proposes a model for implementing an automated attendance management 
system for entities in different areas by making use of face recognition technique, 
implementing Transfer Learning using VGG16 with Deep Convolution Neural Network. 
This model incorporates a Closed-Circuit Television (CCTV) that captures live video, 
Multi-Task Cascaded Convolutional Neural Networks (MTCNN) to detect face from input 
video in real time, recognize the face and mark attendance in the database.

## Objectives 

The primary objective of this project is
-To make the attendance marking system automated and more efficient.

## Applications

This project can be implemented in following application areas:
- For educational institutions using this approach, they can track and maintain 
attendance of students and staffs.
- In companies, this model keeps track of the time employees work and the time they 
take off.


## Dataset

Images of our 15 classmates, 40 of each was captured from our laptop’s webcam using 
python script implementing OpenCV. Later face was cropped from every image in the
collected dataset using python script implementing OpenCV. And then we arranged those 
collected dataset by splitting datasets into train and validation dataset manually with a folder 
of each. Each folder contains 15 sub folders having dataset of each individual in each sub 
folder. The dataset will be made available for further research and development.

## Limitations of Project

This project is limited only to certain number of students for attendance. We need to train 
our model again if we need to add more students.

## Future Enhancement

With more resources and efforts, future enhancements can be done to our project. Later, we 
can make our model better by feeding it with more data while training. Similarly, the 
limitation on the resource i.e., CCTV to capture video in spite of laptop’s webcam can be 
resolved. On the other hand, cloud server can be used for database, parents’ & students’ 
email can be integrated with attendance system and along with some other modifications in 
the frontend.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   https://github.com/Aryal-Rupesh/Real-Time-Face-Recognition-System-Using-Deep-Learning.git 
   

## Example usage
```bash 
python manage.py runserver
```
We welcome contributions to this project. To contribute, follow these steps:

Fork the repository
Create a new branch for your feature or bug fix
Make your changes
Submit a pull request

