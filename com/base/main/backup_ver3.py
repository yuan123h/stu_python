#!/use/bin/python
#Filename: backup_ver1.py

import os
import time

source = ['/home/hadoop/hadoop/conf', '/home/hadoop/hadoop/bin']
# this dir must exit
target_dir = '/home/hadoop/backup/'
today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment --> ')
if len(comment) == 0 :
	target = today + os.sep + now + '.zip'
else :
	target = today + os.sep + now + comment.replace(' ', '_') + '.zip'


if not os.path.exists(today):
	os.mkdir(today)
	print 'successful to create dir ', today

# back dirs
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0 :
	print 'successful backup to', target
else :
	print "backup failed"
	
	
