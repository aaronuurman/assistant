#!/usr/bin/env python3

import os
from slugify import slugify

class CreateNewBranch:
	def __init__(self, title, project_path):
		self.start_message = 'Starting new git branch creation.'
		self.__branch_name = 'post-%s' % slugify(title)
		self.__project_path = project_path

	def execute(self):
		command = 'cd %s && git checkout -B %s' % (self.__project_path, self.__branch_name)
		os.system(command)
		
		return 'Git: Created a new working branch "%s".' % self.__branch_name