#!/usr/bin/env python3

import unittest, os, shutil
from assistant.commands.blog.tasks.download_img import DownloadImg

class TestDownloadImg(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		os.mkdir('/tmp/blog')
		os.mkdir('/tmp/blog/src')
		os.mkdir('/tmp/blog/src/images')
	
	def test_unsplash_url_download_img_success(self):
		#Arrange
		project_path = '/tmp/blog'
		image_url = 'https://unsplash.com/photos/AhC4pduPcGU'
		title = 'Temporary Testing'
		downloadTask = DownloadImg(project_path, image_url, title)
		#Act
		downloadTask.execute()
		#Assert
		self.assertTrue(os.path.isfile('/tmp/blog/src/images/temporary-testing.jpg'))

	@classmethod
	def tearDownClass(cls):
		shutil.rmtree('/tmp/blog')

if __name__ == '__main__':
	unittest.main()