#!/usr/bin/env python3
import os

def createNewBranch(title):
	str = 'post-%s' % title
	command = 'git checkout -B ' + str
	os.system(command)
	return str