# 📷 Webcam Alert App

The **Webcam Alert App** is a Python-based security tool that monitors your webcam for motion and sends email alerts when movement is detected. It's designed for users who want a simple yet effective way to keep an eye on their surroundings using their computer's webcam.

---

## 📑 Contents

- [User Experience](#user-experience-ux)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Application Structure](#application-structure)
  - [Email Notification System](#email-notification-system)
- [Features](#features)
  - [Implemented Features](#implemented-features)
  - [Planned Improvements](#planned-improvements)
- [Technologies Used](#technologies-used)
  - [Languages](#languages-used)
  - [Libraries](#libraries-used)
- [Project Files](#project-files)
- [Installation & Usage](#installation--usage)
  - [Prerequisites](#prerequisites)
  - [How to Run](#how-to-run)
- [Testing](#testing)
- [Credits](#credits)
  - [Code](#code)
  - [Acknowledgements](#acknowledgements)

---

## 🧠 User Experience (UX)

### User Stories

As a user, I want to:

- Monitor my environment using my computer's webcam.
- Receive email alerts when motion is detected.
- Configure the application easily without extensive technical knowledge.
- Ensure that the application runs efficiently in the background.

---

## 🎨 Design

### Application Structure

The application consists of two main components:

1. **Motion Detection**: Utilizes the webcam to detect movement by comparing video frames.
2. **Email Notification**: Sends an email alert with an image attachment when motion is detected.

### Email Notification System

- **SMTP Protocol**: The application uses SMTP to send emails.
- **Configuration**: Users can set their email credentials and recipient address in the `emailing.py` file.
- **Attachments**: Captured images are attached to the email for visual confirmation.

---

## 🛠 Features

### Implemented Features

- ✅ Real-time motion detection using webcam feed.
- ✅ Email alerts with image attachments upon detecting motion.
- ✅ Configurable email settings for sender and recipient.
- ✅ Lightweight and efficient performance.

### Planned Improvements

- 🔄 Add GUI for easier configuration and control.
- 🔄 Implement logging system for activity tracking.
- 🔄 Enable video recording upon motion detection.
- 🔄 Support multiple camera inputs.

---

## 💻 Technologies Used

### Languages Used

- Python 3.13

### Libraries Used

| Library    | Purpose                              |
| ---------- | ------------------------------------ |
| `cv2`      | Accessing and processing webcam feed |
| `smtplib`  | Sending emails via SMTP              |
| `email`    | Constructing email messages          |
| `datetime` | Handling timestamps for alerts       |
| `os`       | File system operations               |

---

## 📁 Project Files

```bash
.
├── main.py # Main script for motion detection
├── emailing.py # Handles email notifications
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---

## 🚀 Installation & Usage

### Prerequisites

Ensure Python 3.13 is installed on your system. Then, install the required packages:

```bash
pip install -r requirements.txt
```

### How to Run

Configure Email Settings:

1. Open emailing.py.

Set your email credentials:

```bash
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
RECIPIENT_ADDRESS = 'recipient@example.com'
```

Note: For Gmail users, you might need to enable "Less secure app access" or use an app password.

2. Run the Application:

```bash
python main.py
```

The application will start monitoring your webcam for motion. When movement is detected, an email alert will be sent to the specified recipient.

## ✅ Testing

Manual testing was conducted to ensure:

- Webcam initializes correctly and captures video feed. ✔
- Motion detection accurately identifies movement. ✔
- Email alerts are sent promptly with correct attachments. ✔
- Application handles exceptions and errors gracefully. ✔

## 🧾 Credits

### Code

- Developed using Python and OpenCV for motion detection.
- Email functionality implemented using Python's built-in libraries.

### Acknowledgements

- Inspired by the need for simple home security solutions.
- Thanks to the open-source community for providing the tools and resources that made this project possible.
