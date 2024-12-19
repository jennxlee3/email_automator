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
def message(subject="Python Notification", text="", img=None, attachment=None):
    msg = MIMEMultipart()
    msg['Subject'] = subject

    # add text content
    msg.attach(MIMEText(text))

    if img is not None:
        if type(img) is not list:
            img = [img]

            for one_img in img:
                img_data = open(one_img, 'rb').read()
                msg.attach(MIMEImage(img_data, name=os.path.basename(one_img)))

    if attachment is not None:
        if type(attachment) is not list:
            attachment = [attachment]
            for one_attachment in attachment:
                with open(one_attachment, 'rb') as f:
                    # read in the attachment
                    file = MIMEApplication(f.read(),
                        name = os.path.basename(one_attachment)
                        )
                    file['Content-Disposition'] = f'attachment;\
            filename="{os.path.basename(one_attachment)}"'

                    msg.attach(file)
    return msg


