import os
import smtplib
import imghdr
from dotenv import load_dotenv
from email.message import EmailMessage

# Load environment variables from .env file
load_dotenv()

# Load credentials and recipient info
PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# Function to send an email with an image attachment
def send_email(image_path):
    # Create email message object
    email_message = EmailMessage()
    email_message["Subject"] = "Object Detected"
    email_message.set_content("An object has been detected in the video feed.")

    # Read the image file and attach it to the email
    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    # Connect to Gmail SMTP server and send the email
    gmail_server = smtplib.SMTP("smtp.gmail.com", 587)
    gmail_server.ehlo()
    gmail_server.starttls()
    gmail_server.login(EMAIL_SENDER, PASSWORD)
    gmail_server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, email_message.as_string())
    gmail_server.quit()

# For testing: run the send_email function directly if this script is run as main
if __name__ == "__main__":
    send_email(image_path="images/15.png")
