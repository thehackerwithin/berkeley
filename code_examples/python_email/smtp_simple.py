import smtplib
from getpass import getpass

# Set the email addresses
fromaddr = 'rossbar15@gmail.com'	# Address of sender
toaddrs = ['rossbar@berkeley.edu']	# List of addresses of recipients

# Construct the email message
# Create message header
msg = "From: %s\nTo: %s\n\n" %(fromaddr, toaddrs)
# The body of the email
body = "Hello %s! Coming to you from %s.\n" \
       %(toaddrs[0], fromaddr)
# Put the whole message together
msg += body

# Setup the smtp server
username = 'rossbar15@gmail.com'		# My gmail name
passwd = getpass('Password for %s: '%username)	# My gmail password
print 'Opening Server connection...'
server = smtplib.SMTP('smtp.gmail.com:587')	# The gmail smtp server
print 'Starting TLS...'
server.starttls()	# For security: All following commands are encrypted
print 'Logging in...'
server.login(username, passwd)	# Connection should be secure before this step

# Send the email
print 'Login Successful, sending message...'
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
print 'Server connection closed.'
