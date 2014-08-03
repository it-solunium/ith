#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from misc import bcolors, misc
from config import bddConfiguration
import os

misc_instance = misc()
connexionParameters = []
connexionParameters = misc.readConfFile(misc_instance, "BddConfig")

# Create database
print "["+bcolors.OKBLUE+"-"+bcolors.ENDC+"] Creating database %s" % bddConfiguration.db
cmd_create_db = 'echo "create database %s" | mysql -u%s -p%s' % (bddConfiguration.db, bddConfiguration.user, bddConfiguration.passwd)
os.system(cmd_create_db)

# Import dump file : google_dorks.sql
print "["+bcolors.OKBLUE+"-"+bcolors.ENDC+"] Importing dorks from dump."
cmd_import_dump = "mysql -u%s -p%s %s < ./google_dorks.sql" % (bddConfiguration.user, bddConfiguration.passwd, bddConfiguration.db)
os.system(cmd_import_dump)

