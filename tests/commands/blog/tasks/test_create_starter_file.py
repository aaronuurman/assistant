#!/usr/bin/env python3

import unittest, os, shutil
from datetime import datetime
from assistant.commands.blog.dto.image_dto import ImageDto
from assistant.commands.blog.tasks.create_starter_file import CreateStarterFile

class TestCreateStarterFile(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		os.mkdir('/tmp/blog')
		os.mkdir('/tmp/blog/src')
		os.mkdir('/tmp/blog/src/pages')
		os.mkdir('/tmp/blog/src/pages/posts')
	
	def test_correct_execute_success(self):
		#Arrange
		title = 'Test title'
		project_path = '/tmp/blog'
		date = datetime.now().strftime('%Y-%m-%d')
		image = ImageDto(
			'test-title.jpg',
			'https://unsplash.com/photos/_epQ6P-wMeE',
			'Mohammed Hassan',
			'https://unsplash.com/@moh_ph'
		)
		task = CreateStarterFile(title, project_path)
		#Act
		result = task.execute(image)
		#Assert
		self.assertEqual(('File creation: Starter file for blog post created to "/tmp/blog/src/pages/posts/%s-test-title.md"' % date), result)
		self.assertTrue(os.path.isfile('/tmp/blog/src/pages/posts/%s-test-title.md' % date))

	@classmethod
	def tearDownClass(cls):
		shutil.rmtree('/tmp/blog')

if __name__ == '__main__':
	unittest.main()