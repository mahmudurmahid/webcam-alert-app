import os
import smtplib
import imghdr
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Object Detected"
    email_message.set_content("An object has been detected in the video feed.")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail_server = smtplib.SMTP("smtp.gmail.com", 587)
    gmail_server.ehlo()
    gmail_server.starttls()
    gmail_server.login(EMAIL_SENDER, PASSWORD)
    gmail_server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, email_message.as_string())
    gmail_server.quit()

if __name__ == "__main__":
    send_email(image_path="images/15.png")
