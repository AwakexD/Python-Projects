import smtplib
import ssl
from email.message import EmailMessage

subject = "Python email"
body = "Test email"
sender_email = ""  # Enter sender email
reciver_email = ""  # Enter reciver email

password = input("Enter your password: ")

message = EmailMessage()
message['From'] = sender_email
message['To'] = reciver_email
message['Subject'] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email...")
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciver_email, message.as_string())
    print("Success")
