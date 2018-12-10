import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def Email():
    #you will need to turn on "Allow less secure apps" for this to work.
    fromaddr = "clintonattendance@gmail.com"
    toaddr = "clintonattendance@gmail.com"
 
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
    server.login(fromaddr, "27Berkshire")#your email's password
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

Email()
