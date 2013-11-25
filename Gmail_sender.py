#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = "my-mail@gmail.com"
gmail_pwd = "my-pass"
print("mail source : ")
mail_from = raw_input()
def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = mail_from
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
  
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())

   mailServer.close()
print("mail dest : ")
mail_dest = raw_input()
mail(mail_dest,
   "subject",
   "Hi this is python",
   "")


