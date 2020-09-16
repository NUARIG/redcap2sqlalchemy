#!/usr/bin/env python

"""You can run this script before an interactive ipython session:

$ ipython -i demoscripts.py
"""

import configparser as cp
import redcap2sqlalchemy as rc2sa
import sqlalchemy as sa

myconfig = cp.ConfigParser()
myconfig.read('config.ini')

myrcproject = rc2sa.rcproject_from_config(myconfig['REDCAP'])

mysaurl = sa.engine.url.URL(
    myconfig['DATABASE']['sqlalchemy.drivername'],
    username=myconfig['DATABASE']['sqlalchemy.username'],
    password=myconfig['DATABASE']['sqlalchemy.password'],
    host=myconfig['DATABASE']['sqlalchemy.host'],
    database=myconfig['DATABASE']['sqlalchemy.database']
)

mysaengine = sa.create_engine(mysaurl)
mymetadata = sa.MetaData(mysaengine)


