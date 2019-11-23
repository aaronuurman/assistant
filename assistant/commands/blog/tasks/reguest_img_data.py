#!/usr/bin/env python3

from slugify import slugify
from bs4 import BeautifulSoup
from urllib import request, parse
from assistant.common import logger
from assistant.commands.blog.dto.image_dto import ImageDto

class RequestImageData:
	def __init__(self, img_url, title, config):
		self.start_message = 'Requesting image data.'
		self.__img_url = img_url
		self.__file_name = '.'.join((slugify(title),'jpg'))
		self.__is_verbose = config.verbose

	def execute(self):
		"""Request image data from provided url.
		
		Returns: Request result.
		"""
		
		img_url = self.__img_url
		file_name = self.__file_name
		is_verbose = self.__is_verbose

		image = self.__get_data(img_url, file_name)
		logger.info(is_verbose, 'Image url: %s' % image.url)
		logger.info(is_verbose, 'Image file name: %s' % image.file_name)
		logger.info(is_verbose, 'Image author: %s' % image.author_name)
		logger.info(is_verbose, 'Image author profile: %s' % image.author_profile)

		return 'Request: Successfully aquired image data from %s' % img_url, image

	def __get_data(self, imageUrl, file_name):
		selector = '_3XzpS _1ByhS _4kjHg _1O9Y0 _3l__V _1CBrG xLon9'
		response = request.urlopen(imageUrl)

		if response.code != 200:
			raise Exception('Failed to make request to "%s"' % imageUrl)

		data = response.read()
		html = data.decode('UTF-8')
		soup = BeautifulSoup(html, "html.parser")
		anchor = soup.find('a', class_=selector)
		username = anchor['href'].lstrip('/')
		author = anchor.contents[0]
		parsed_uri = parse.urlparse(imageUrl)
		author_profile = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
		image = ImageDto(file_name, imageUrl, author, (author_profile + username))

		return image