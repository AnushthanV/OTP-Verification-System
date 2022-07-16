import optparse
import random
import smtplib
import re
from email.message import EmailMessage

otp = str(random.randrange(100000, 999999))
emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

valid = False
while valid == False:
    email = str(input("Enter your email address: "))
    
    if(re.fullmatch(emailRegex, email)):
        valid = True
    else:
        print("Invalid email. Please enter a valid email.")

sender = "YOUR EMAIL ADDRESS"
receiver = email
msg = EmailMessage()
msg.set_content(f"This is the OTP for verfication: \n {otp}")
msg['Subject'] = "OTP for verification"
msg['From'] = sender
msg['To'] = receiver

var = smtplib.SMTP("smtp.gmail.com", 587)
var.starttls()
var.login(sender, "YOUR APP PASSWORD")
var.send_message(msg, sender, receiver)         
print("Successfully sent OTP, check your email.")

done = False
while done == False:
    verify = str(input("Enter OTP: "))
    if verify == otp:
        print("Correct OTP, verification successful!")
        done = True
    elif verify != otp:
        print("Incorrect OTP, please try again.")