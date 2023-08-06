import json
import logging
import os
from collections import OrderedDict
from io import StringIO
from tempfile import TemporaryDirectory
from time import sleep
from typing import Any, AnyStr, Dict, Iterable, List, Optional, Set, Tuple, Union

import pandas as pd
import requests

# # dccs
# https://great-help.atlassian.net/wiki/spaces/GREAT/pages/655447/Programming+Interface
# creat a file called joblist, each row looks like this
# results1.tsv http://bejerano.stanford.edu/great/public/cgi-bin/greatStart.php?outputType=batch&requestSpecies=hg18&requestName=Example+Data&requestSender=Client+A&requestURL=http%3A%2F%2Fwww.clientA.com%2Fdata%2Fexample1.bed
# results2.tsv http://bejerano.stanford.edu/great/public/cgi-bin/greatStart.php?outputType=batch&requestSpecies=hg18&requestName=Example+Data&requestSender=Client+A&requestURL=http%3A%2F%2Fwww.clientA.com%2Fdata%2Fexample2.bed

# Then run the script
# ./greatBatchQuery.py joblist
#!/usr/bin/env python

import sys;
from threading import Thread;
import urllib;
import time;

if len(sys.argv) != 2:
	sys.stderr.write("Usage: %s <joblist>\n" % (sys.argv[0]))
	sys.exit(1)

NUM_REQUESTS = 5 # hard limit by great server, raising this will not get more jobs since the server will deny requests
JOBLIST = open(sys.argv[1]).readlines()

def main():
	for r in range(NUM_REQUESTS):
		t = Agent(JOBLIST[r::NUM_REQUESTS]) # split job list into the number requests possible
		t.start()

class Agent(Thread):
	def __init__(self, joblist):
		Thread.__init__(self)
		self.jobs = []
		self.url_root = "http://bejerano.stanford.edu/great/public/cgi-bin/greatStart.php?"
		bed = ''
		params = {
			'requestURL': bed, # The URL for the BED data to process.
			'outputType': 'batch', # or 'web'
			'requestSpecies': 'hg38',
			'requestName': 'Example',
			'requestSender': 'ClientA', # The name of the tool submitting the data, which is used as a prefix to requestName to identify the data on the GREAT output page.
			#'bgURL': '', # The URL for the BED data used as the background for the foreground/background test.
			#'bgName': '', # he name used to identify the background BED data on the GREAT output page. If not given, "external background data" is used.
		}
		self.params = urllib.parse.urlencode(params)
		# for job in joblist:
		# 	self.jobs.extend(map(lambda x: x.strip().split(), joblist))
	
	def run(self):
		for output, url in self.jobs:
			req = urllib.Request(url)
			retry = True
			while retry:
				try:
					retry = False
					result = urllib.urlopen(req)
				except urllib.HTTPError as error: 
					if(error.getcode() != 500):
						sys.stderr.write("Expected Error: [HTTP Error 500: Internal Server Error]. Actual Error: [%s].\n" % (error))
						sys.stderr.write("\tQuitting due to unexpected error.\n")
						sys.exit(1)
					#sys.stderr.write("[%s] for output [%s]. Server likely busy. Will retry.\n" % (error, output));	# Remove comment if you want to see retries
					retry = True
					time.sleep(10); # if request gets denied, wait 10 seconds and try again
				if(not retry):
					f = open(output, 'w')
					f.write(result.read())
					f.close()
					print("STATUS: Done, REQUEST: %s, OUTPUT: %s" % (url, output))

if __name__ == '__main__':
	main()
