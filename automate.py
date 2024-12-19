from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
import os

# connect to email server
smtp = smtplib.SMPT('smtp-mail.outlook.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('jennifer.lee0721@outlook.com', 'Jhboryl0105!')

# build message content

