import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

mailc = input("Pour : ")
objet = input("Objet : ")
message = input("Message : ")
print()
confirm = input("Envoyer ? (y/n) : ")


msg = MIMEMultipart()
msg['From'] = 'XXX@gmail.com'
msg['To'] = mailc
msg['Subject'] = objet
message = message
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('XXX@gmail.com', 'PASSWORD')
mailserver.sendmail('XXX@gmail.com', 'XXX@gmail.com', msg.as_string())
mailserver.quit()
