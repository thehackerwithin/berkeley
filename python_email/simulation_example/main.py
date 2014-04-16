# Example script showing how to run a program, collect some run statistics, and
# have the script email when the program is done. Here a simple simulation
# is written in python for demonstration purposes, but any run command can be
# used in it's stead. In this example, we use the subprocess module to run the
# simulation program instead of importing the functions and calling them here
# to show what you would do for a third party application

from __future__ import division

# Imports for the simulation and run logging
import numpy as np
import subprocess
import time
import os
import psutil
# Imports for the email notification
import smtplib
from getpass import getpass
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formatdate
from email import Encoders

# Run the simulation
simulation_output = open('sim_out.txt', 'w')
spawner = subprocess.Popen('python chirikov.py', stdout=simulation_output,\
                 shell=True)

# Do some logging of the simulation while it's running
proc_monitor = psutil.Process(spawner.pid)
time.sleep(1)	# This is a hack to ensure the child process has been spawned by
	        # Popen
runtime = []
cpu_percent = []
mem_percent = []
while proc_monitor.status() != 'zombie':
  try:
    p = psutil.Process(spawner.pid+1)
    cpu_percent.append(p.cpu_percent(1.0))
    mem_percent.append(p.memory_percent())
    runtime.append(time.time()-p.create_time())
  except psutil.NoSuchProcess: break
print 'Simulation Complete!'

# Write the stats out in csv format
data = np.zeros((len(cpu_percent),3))
for col, d in enumerate((runtime, cpu_percent, mem_percent)):
  data[:,col] = d
np.savetxt('sim_stats.csv', data, fmt='%.2f', delimiter=',')

# Compose the email
fromaddr = 'grim4cci2@gmail.com'
toaddrs = ['rossbar15@gmail.com']
msg = MIMEMultipart()
msg['To'] = ", ".join(toaddrs)
msg['From'] = fromaddr
msg['Subject'] = 'Chirikov Simulation Complete!'
msg['Date'] = formatdate()
text = '''
Simulation completed in %.2f seconds. Results are attached in
chirikov_results.png. The text output from the simulation is in sim_out.txt.
Some tracked simulation stats are in the attached sim_stats.csv.
''' % runtime[-1]
# Create message body
body = MIMEText(text, 'plain')
msg.attach(body)
# Attach image
results = open('chirikov_results.png', 'rb').read()
img = MIMEImage(results)
msg.attach(img)
# Attach Simulation output
for f in ("sim_out.txt", "sim_stats.csv"):
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(open(f, 'rb').read())
  Encoders.encode_base64(part)
  part.add_header('Content-Disposition', 'attachment; filename="%s"'\
                  % os.path.basename(f))
  msg.attach(part)

# Send email
username = fromaddr
#NOTE: For an automated email sender, you obviously can't use getpass (which is
#interactive) to send the email. Other solutions include secure password 
#storage with gpg or making a dummy email account.
passwd = getpass('Password for %s: '%username)
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, passwd)
print 'Sending message...'
server.sendmail(fromaddr, toaddrs, msg.as_string())
server.quit()
print 'Message sent!'
