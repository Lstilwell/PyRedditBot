import smtplib


def send_mail(sub):
	message = "new post on " + sub + "\n http://reddit.com/r/"+sub
	subject = "New Reddit Post"
	content = 'Subject: %s\n\n%s' % (subject, message)

	print(content)
	
	mail = smtplib.SMTP('smtp.gmail.com',587)

	mail.ehlo()

	mail.starttls()

	mail.login('email','password')

	mail.sendmail('sender email', 'receiver email', content)

	mail.close()
