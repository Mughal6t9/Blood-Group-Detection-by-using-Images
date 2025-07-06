Blood Group Detection System
Overview
This project is a web-based application that detects blood groups from images of blood samples using YOLOv8 object detection model. The system provides a professional hospital report with patient information, detected blood group, and a QR code for verification.

Features
🔐 Secure login system for authorized personnel
    Username: admin
    Password: 1234

🩸 Blood group detection using YOLOv8 model

📝 Automatic PDF report generation with:

Patient details (name, age, gender)

Detected blood group with components

QR code for verification

Professional hospital letterhead

📂 Image upload and processing interface

📊 Clear visualization of detection results

Installation
Clone the repository:

bash
git clone https://github.com/Mughal6t9/Blood-Group-Detection-by-using-Images
cd blood-group-detection
Install required dependencies:

bash
pip install -r requirements.txt
Download the pre-trained YOLO model weights or train your own (see Training section below).

Usage
Run the Streamlit application:

bash
streamlit run index.py
Login with the default credentials:

Username: admin
Password: 1234

Follow the on-screen instructions:
•	Enter patient information
•	Upload blood sample image
•	View detection results
•	Download the PDF report

Training the Model
To train or retrain the YOLO model:
Prepare your dataset with proper annotations
Configure the data.yaml file
Run the training script:

bash
python train.py
File Structure
blood-group-detection/
├── index.py            # Main Streamlit application
├── train.py            # Model training script
├── output/             # Directory for processed images and reports
├── requirements.txt    # Python dependencies
└── README.md           # This file

Requirements Librarys
Python 3.8+
Streamlit
PyTorch
Ultralytics YOLOv8
Pillow (PIL)
fpdf2
qrcode

Notes
The current implementation uses a pre-trained model path (E:\Blood Group Detection (Images)\runs\detect\train\weights\best.pt) which should be updated to match your local path or repository structure.

For production use, change the default login credentials in index.py.

The system currently supports detection of all major blood groups (A, B, AB, O) with positive and negative Rh factors.
License
This project is open-source and available under the MIT License.
