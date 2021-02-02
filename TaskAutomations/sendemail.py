import os
import smtplib 
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

contacts = ['email', 'email', 'email']

msg = EmailMessage()
msg['Subject'] = 'Check this out'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ''.join(contacts)
msg.set_content("Check this amazing picture out")

files = ['amazingPicture.png']

for file in files: 
	with open(file, 'rb') as f: 
		file_date = f.read()
		file_type = imghdr.what(f.name)
		file_name = f.name

	msg.add_attachment(file_date, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	smtp.send_message(msg)