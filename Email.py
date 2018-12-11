import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os from sys
def Email():
    #you will need to turn on "Allow less secure apps" for this to work.
    
    fromaddr = input("What is your email?")
    toaddr = input("Who are you sending this to?")
 
    msg = MIMEMultipart()
 
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = input("What would you like your subject to be?")
 
    body = input("What would your email body would like to be? Please type your answer.") 
 
    msg.attach(MIMEText(body, 'plain'))
 
    filename = "Timesheet.txt"
    attachment = open("TimeSheet.txt", "rb")
 
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
    msg.attach(part)
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    password = input("What is your password? Do not worry, this will never save.")
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
start = input("Hello! Would you like to send an email? Y or N")
if start == "Y":
                 Email()
else:
                 print("Ok! Hope to see you soon!")
                 sys.exit(0)
                
                 
