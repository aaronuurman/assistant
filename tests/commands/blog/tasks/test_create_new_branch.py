#!/usr/bin/env python3

import unittest, os, shutil
from assistant.commands.blog.tasks.create_new_branch import CreateNewBranch

class TestCreateNewBranch(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		os.mkdir('/tmp/blog')
		os.system('git init /tmp/blog/')
	
	def test_title_create_new_branch_success(self):
		#Arrange
		title = 'Test title'
		task = CreateNewBranch(title, '/tmp/blog/')
		#Act
		result = task.execute()
		#Assert
		self.assertEqual('Git: Created a new working branch "post-test-title".', result)
	
	@classmethod
	def tearDownClass(cls):
		shutil.rmtree('/tmp/blog')

if __name__ == '__main__':
	unittest.main()