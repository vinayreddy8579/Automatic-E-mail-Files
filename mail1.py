import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "vinayr.kandula@gmail.com"
receiver_email = "vinay.kandula@us.abb.com"
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "Test email"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message

html = """\
<html>
  <body>
    <p>Hi Vinay,<br>
       You have yet to complete the requests TMS3001, TMS3003. which was due for 4 days.
       Follow the link to the open ticket<br>
       <a href="http://10.90.83.63/request/3001">here</a> 
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )