#!/usr/bin/env python3

import os, unittest, shutil
from assistant.commands.blog.tasks.validate_project_path import ValidateProjectPath

class TestValidateProjectPath(unittest.TestCase):

	def setUp(self):
		self.project_path = '/tmp/blog'

	def test_empty_string_validate_project_path_error(self):
		#Setup
		os.mkdir(self.project_path)
		#Arrange
		task = ValidateProjectPath("")
		#Act
		with self.assertRaises(ValueError) as value_error:
			task.execute()

		exception_message = value_error.exception.args[0]
		#Assert
		self.assertEqual('Path to blog project is required.', exception_message)
		#Teardown
		shutil.rmtree(self.project_path)

	def test_missing_image_folder_validate_project_path_error(self):
		#Setup
		os.mkdir(self.project_path)
		#Arrange
		task = ValidateProjectPath(self.project_path)
		#Act
		with self.assertRaises(ValueError) as value_error:
			task.execute()

		exception_message = value_error.exception.args[0]
		#Assert
		self.assertEqual('Blog project does not contain folder "images".', exception_message)
		#Teardown
		shutil.rmtree(self.project_path)

	def test_project_path_validate_project_path_success(self):
		#Setup
		os.mkdir(self.project_path)
		os.mkdir((self.project_path+"/src"))
		os.mkdir((self.project_path+"/src/images"))
		#Arrange
		task = ValidateProjectPath(self.project_path)
		#Act
		result = task.execute()
		#Assert
		self.assertEqual('Validation: Project path "/tmp/blog" is valid.', result)
		#Teardown
		shutil.rmtree(self.project_path)

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()