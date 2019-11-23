#!/usr/bin/env python3

import os
from slugify import slugify

class CommitPushChanges:
	def __init__(self, project_path, title):
		self.start_message = "Starting to commit and push changes."
		self.__project_path = project_path
		self.__title = title
		self.__branch = 'post-%s' % slugify(title)

	def execute(self):
		add_command = 'cd %s && git add .' % self.__project_path
		os.system(add_command)
		commit_command = 'cd %s && git commit -m "Create blog post starter files for %s"' % (self.__project_path, self.__title)
		os.system(commit_command)
		push_command = 'cd %s && git push --set-upstream origin %s' % (self.__project_path, self.__branch)
		os.system(push_command)

		return 'Git: Changes are commited and pushed to %s' % self.__branch	