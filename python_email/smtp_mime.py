import smtplib
from getpass import getpass
# Import MIME classes to help with message construction
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import email.utils

fromaddr = 'rossbar15@gmail.com'
toaddrs = ['rossbar@berkeley.edu']
ccaddr = 'RWBarnowski@lbl.gov'

# Put the message together, starting with the header
msg = MIMEMultipart()	# Access header fields like a python dictionary (key/value pairs)
msg['To'] = ", ".join(toaddrs)
msg['From'] = fromaddr
msg['Subject'] = 'Our First Complex Message'
msg['Cc'] = ccaddr
msg['Date'] = email.utils.formatdate()

# Let's say we want are message to be html instead of plain text, with 
# the MIMEText object, that's no problem!

# Load the html message you want to send
html_file = open('sample_message.html', 'r')
html_msg = html_file.read()
html_file.close()
# Load it into the appropriate MIME type
body = MIMEText(html_msg, 'html') # Explicitly define subtype
# Attach the text object to the main message
msg.attach(body)

# Let's also add an image to our message
imgfile = open('run_away.gif', 'rb')
img = imgfile.read()
imgfile.close()
# Let MIMEIMage determine the subtype for us
img_a = MIMEImage(img)
# Attach our image to the main message
msg.attach(img_a)

# Now that our message is put together, send it!
username = 'rossbar15@gmail.com'
passwd = getpass('Password for %s: '%username)
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, passwd)
# Note the .as_string on the msg object!
print 'Sending message...'
server.sendmail(fromaddr, toaddrs, msg.as_string())
server.quit()
print 'Message sent!'
