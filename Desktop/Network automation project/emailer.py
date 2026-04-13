import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from configuration import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER
from logger import logger

def send_email(subject, body, to_email):
    from_email = EMAIL_SENDER
    email_password = EMAIL_PASSWORD

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))
     
    try:

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
           server.starttls()
           server.login(from_email, email_password)
           server.send_message(msg)
           logger.info(f"Email sent to {to_email}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
   