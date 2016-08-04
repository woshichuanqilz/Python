# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
textfile = 'sendmail.py'
fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = 'imlegendlzz@gmail.com'
msg['To'] = 'imlegendlzz@gmail.com'

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('smtp.gmail.com')
s.ehlo()
s.starttls()
s.login('imlegendlzz@gmail.com', 'woshihuanhuan226')
s.sendmail('imlegendlzz@gmail.com', 'imlegendlzz@gmail.com', msg.as_string())
s.quit()
