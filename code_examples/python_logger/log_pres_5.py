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
log.debug( "This is the debug level on root reporting in" )
log.info( "This is the info level on root reporting in " )
log.warning( "This is the warning level on root reporting in" )
log.error( "This is the error level on root reporting in" )
log.critical( "This is the critical level on root reporting in" )

# Create a new log class instance. Why, it can have
# different behaviors than the root logger
new_instance_log = log.getLogger( 'new' )

# Set the new instance's log level as well as format with .basicConfig
new_instance_log.setLevel( 10 )

# Some sample messages. Can you guess which will print?
new_instance_log.debug( "This is the debug level on new reporting in" )
new_instance_log.info( "This is the info level on new reporting in " )
new_instance_log.warning( "This is the warning on new level reporting in" )
new_instance_log.error( "This is the error level on new reporting in" )
new_instance_log.critical( "This is the critical level on new reporting in" )

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

# Set the base level for this instance much higher so we don't
# reprint to screen
new_instance_log.setLevel(80)

# Some sample messages. Can you guess which will print, and to where?
new_instance_log.debug( "This is the debug level reporting in" )
new_instance_log.info( "This is the info level reporting in " )
new_instance_log.warning( "This is the warning level reporting in" )
new_instance_log.error( "This is the error level reporting in" )
new_instance_log.critical( "This is the critical level reporting in" )
