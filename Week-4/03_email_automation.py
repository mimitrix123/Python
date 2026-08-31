"""Week 4 Practice 3: Email Automation using smtplib.
Update EMAIL and APP_PASSWORD before running.
"""

import smtplib
from email.mime.text import MIMEText

EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"


def send_email(receiver, subject, message):
    email = MIMEText(message)
    email["Subject"] = subject
    email["From"] = EMAIL
    email["To"] = receiver

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(email)


if __name__ == "__main__":
    print("Configure EMAIL and APP_PASSWORD before sending emails.")
