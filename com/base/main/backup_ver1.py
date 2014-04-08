#!/use/bin/python
#Filename: backup_ver1.py

import os
import time

source = ['/home/hadoop/hadoop/conf']
target = '/home/hadoop/backup'
target = target + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 备份了所有目录
zip_command = "zip -qr '%s' %s" % (target, ''.join(source))

if os.system(zip_command) == 0 :
	print 'successful backup to', target
else :
	print "backup failed"
	
	
