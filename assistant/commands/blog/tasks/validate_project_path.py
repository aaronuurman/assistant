#!/usr/bin/env python3

from assistant.common.file_handler import find_sub_folder
from assistant.common.str_helper import is_null_or_whitespace

class ValidateProjectPath:
	def __init__(self, project_path):
		self.start_message = 'Starting project path validation.'
		self.__project_path = project_path
	
	def execute(self):
		"""Validate project path.
		-required
		-should contain a 'images' folder

		returns:
			Validation success message.
		"""
		path = self.__project_path

		if is_null_or_whitespace(path):
			raise ValueError('Path to blog project is required.')

		if not find_sub_folder(path, '/src/images'):
			raise ValueError('Blog project does not contain folder "images".')

		if not find_sub_folder(path, '/src/pages/posts'):
			raise ValueError('Blog project does not contain folder "posts".')

		return 'Validation: Project path "%s" is valid.' % path