#!/usr/bin/env python3

from os import path
from urllib import request
from slugify import slugify
from assistant.common import file_handler

class DownloadImg:
	def __init__(self, path, img_url, title):
		self.start_message = 'Starting image download.'
		self.__project_path = path
		self.__img_url = img_url
		self.__download_url = img_url + '/download?force=true'
		self.__file_name = '.'.join((slugify(title),'jpg'))

	def execute(self):
		"""Downloads a image from provided url to a provided location.
		
		Returns: Request result.
		"""

		full_image_path = path.join(file_handler.find_sub_folder(self.__project_path, '/src/images'), self.__file_name)
		request.urlretrieve(self.__download_url, full_image_path)

		return 'Image "%s" downloaded succesfully to "%s".' % (self.__img_url, full_image_path)