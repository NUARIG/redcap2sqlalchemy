#!/usr/bin/env python

"""You can run this script before an interactive ipython session:

$ ipython -i demoscripts.py
"""

import configparser as cp
import redcap2sqlalchemy as rc2sa
import sqlalchemy as sa
import logging
import sys

# Set up the logger and parse the configuration
logging.basicConfig(level='INFO')
mylogger = logging.getLogger('rc2sa.demo')
myconfig = cp.ConfigParser()
myconfig.read('config.ini')
mylogger.info("Parsed config.ini")

# Instantiate an RCProject from a connection to live REDCap server
# rc2sa.rcproject_from_config is a convenience function to instantiate the class based on the URL and API key found in config
if 'REDCAP' not in myconfig:
    mylogger.error("Did not find 'REDCAP' configuration in config.ini")
    sys.exit("Missing 'REDCAP' section from config.ini")
    
mylogger.info("'REDCAP' configuration found in config.ini")
myrcproject = rc2sa.rcproject_from_config(myconfig['REDCAP'])
mylogger.info("Instantiated RCProject class based on successful connection")
mylogger.info(myrcproject)

# Set up the SQLAlchemy engine and load the Metadata from the schema
if 'DATABASE' not in myconfig:
    mylogger.error("Did not find 'DATABASE' configuration in config.ini")
    sys.exit("Missing 'DATABASE' section from config.ini")
mylogger.info("'DATABASE' configuration found in config.ini")
mysaurl = sa.engine.url.URL(
    myconfig['DATABASE']['sqlalchemy.drivername'],
    username=myconfig['DATABASE']['sqlalchemy.username'],
    password=myconfig['DATABASE']['sqlalchemy.password'],
    host=myconfig['DATABASE']['sqlalchemy.host'],
    database=myconfig['DATABASE']['sqlalchemy.database']
)
mysaengine = sa.create_engine(mysaurl)
mymetadata = sa.MetaData(mysaengine)
mylogger.info('Connected to DB and imported MetaData object')

