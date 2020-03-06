import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from settings.parseSettings import get_Settings

EMAIL_Settings = get_Settings('EMAIL')
FROM_ADD = EMAIL_Settings['FROM_ADD']
USERNAME = EMAIL_Settings['USERNAME']
PASSWORD = EMAIL_Settings['PASSWORD']
SMTP_SERVER = EMAIL_Settings['SMTP_ADD']
SMTP_PORT = EMAIL_Settings['SMTP_PORT']


class Class_eMail():
	
	def __init__(self):
		self.session = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
		self.session.ehlo()
		self.session.login(USERNAME, PASSWORD)

		
	def initialise_Mail_Body(self, To_Add, Subject):
		#Prepare Mail Body
		Mail_Body = MIMEMultipart()
		Mail_Body['From'] = FROM_ADD
		Mail_Body['To'] = To_Add
		Mail_Body['Subject'] = Subject
		return Mail_Body
	
	
	#Call this to send plain text emails.
	def send_Text_Mail(self, To_Add, Subject, txtMessage):
		Mail_Body = self.initialise_Mail_Body(To_Add, Subject)
		#Attach Mail Message
		Mail_Msg = MIMEText(txtMessage, 'plain')
		Mail_Body.attach(Mail_Msg)
		#Send Mail
		self.session.sendmail(FROM_ADD, [To_Add], Mail_Body.as_string())
	
	
	#Call this to send HTML emails.
	def send_HTML_Mail(self, To_Add, Subject, htmlMessage):
		Mail_Body = self.initialise_Mail_Body(To_Add, Subject)
		#Attach Mail Message
		Mail_Msg = MIMEText(htmlMessage, 'html')
		Mail_Body.attach(Mail_Msg)
		#Send Mail
		self.session.sendmail(FROM_ADD, [To_Add], Mail_Body.as_string())
		

	def __del__(self):
		self.session.close()
		del self.session
