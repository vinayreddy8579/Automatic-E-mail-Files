import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to']=to
    user = "vinayr.kandula@gmail.com"
    msg['from']= user
    password = "nbyscngukisoedbk"
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
	
if __name__ == '__main__':
    
    email_alert("Test Message","Hi Vinay, you have a pending request follow the link","4058564744@tmomail.net")
  