#!/usr/bin/env python

import sys
import time,datetime
from urlparse import urlparse
import re

for line in sys.stdin:
	line = line.strip()
	words = line.split('\t', -1)
	if len(words) < 8:
		continue
	url_s = words[3]
	if (len(url_s) > 0):
		myurl = urlparse(url_s)
		if myurl.hostname == 'financeprod.alipay.com':
			print '%s\t%s'% ('a', 1)
