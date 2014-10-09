#!/usr/bin/python
# Creator: Daniel Wooten
# License: GPL

# import the python logging utility as log
import logging as log

# Use .basicConfig to nicely format our output for the root logger
# as well as set the log level
log.basicConfig( format = '[%(name)s - %(levelname)8s] %(message)s' \
	, level = 10 )
# Some sample messages for the root logger
log.debug( "This is the debug level reporting in" )
log.info( "This is the info level reporting in " )
log.warning( "This is the warning level reporting in" )
log.error( "This is the error level reporting in" )
log.critical( "This is the critical level reporting in" )

# Create a new log class instance. Why, it can have
# different behaviors than the root logger
new_instance_log = log.getLogger( 'seperate_instance' )

# Set the new instance's log level as well as format with .basicConfig
new_instance_log.setLevel( 10 )

# Some sample messages. Can you guess which will print?
new_instance_log.debug( "This is the debug level reporting in" )
new_instance_log.info( "This is the info level reporting in " )
new_instance_log.warning( "This is the warning level reporting in" )
new_instance_log.error( "This is the error level reporting in" )
new_instance_log.critical( "This is the critical level reporting in" )

# Now we create a "handler" for the new instance, this will
# modifty its behavior, most importantly by redirecting the
# output that we specify below
not_serious = log.FileHandler(filename = 'handler_out.txt' , \
	mode = 'w')
# Set the handler's level
not_serious.setLevel( 30 )
# Create a formatter for our handler
ns_formatter = log.Formatter('%(asctime)s - %(message)s')
# Format the handler output
not_serious.setFormatter( ns_formatter )
# This is the real power of handlers
# Add the handler to the new_instance_log
new_instance_log.addHandler(not_serious)

# Some sample messages. Can you guess which will print, and to where?
new_instance_log.debug( "This is the debug level reporting in" )
new_instance_log.info( "This is the info level reporting in " )
new_instance_log.warning( "This is the warning level reporting in" )
new_instance_log.error( "This is the error level reporting in" )
new_instance_log.critical( "This is the critical level reporting in" )
