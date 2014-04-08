#!/use/bin/python
#Filename: backup_ver1.py

import os
import time

source = ['/home/hadoop/hadoop/conf', '/home/hadoop/hadoop/bin']
# this dir must exit
target_dir = '/home/hadoop/backup/'
today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)
	print 'successful to create dir ', today

target = today + os.sep + now + '.zip'

# back dirs
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0 :
	print 'successful backup to', target
else :
	print "backup failed"
	
	
