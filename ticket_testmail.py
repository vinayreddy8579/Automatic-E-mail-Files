import csv, smtplib, ssl

message = """Subject: RE: Pending Tickets

Hi {name}, your pending tickets are {PendingTickets}. Follow the link to redirect to the ticket {Link}"""
from_address = "vinayr.kandula@gmail.com"
password = input("Type your password and press enter: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("Contacts.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, PendingTickets, Link in reader:
            server.sendmail(
                from_address,
                email,
                message.format(name=name,PendingTickets=PendingTickets, Link=Link),
            )