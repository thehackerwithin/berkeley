#!/usr/bin/python
# Creator: Daniel Wooten
# License: GPL

# import the python logging utility as log
import logging as log

# Use .basicConfig to nicely format our output for the root logger
# as well as set the log level and the output file and mode
log.basicConfig( filename = 'log_file.txt' , filemode = 'w' ,
	 format = '[%(name)s - %(levelname)8s] %(message)s', level = 10 )

# Some sample messages for the root logger
log.debug( "This is the debug level reporting in" )
log.info( "This is the info level reporting in " )
log.warning( "This is the warning level reporting in" )
log.error( "This is the error level reporting in" )
log.critical( "This is the critical level reporting in" )

