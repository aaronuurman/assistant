#!/usr/bin/env python3

import unittest
from assistant.commands.blog.tasks.reguest_img_data import RequestImageData
from assistant.dto.config_dto import ConfigDto

class TestRequestImageData(unittest.TestCase):
	def test_unsplash_url_get_image_author_success(self):
		#Arrange
		image_url = 'https://unsplash.com/photos/AhC4pduPcGU'
		title = 'Testing request'
		config = ConfigDto()
		task = RequestImageData(image_url, title, config)
		#Act
		result, image = task.execute()
		#Assert
		self.assertEqual(result, 'Request: Successfully aquired image data from https://unsplash.com/photos/AhC4pduPcGU')
		self.assertEqual(image.author_name, 'NOAA')
		self.assertEqual(image.author_profile, 'https://unsplash.com/@noaa')
		self.assertEqual(image.file_name, 'testing-request.jpg')
		self.assertEqual(image.url, image_url)

if __name__ == '__main__':
	unittest.main()