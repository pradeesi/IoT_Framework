from email_msg.email_handler import Class_eMail

email = Class_eMail()
email.send_Text_Mail('pradeep.si@gmail.com', 'Plain Text Mail', 'This is sample plain test email.')
del email


email = Class_eMail()
email.send_HTML_Mail('pradeep.si@gmail.com', 'HTML Mail', '<html><h1>This is sample HTML test email</h1></html>')
del email