#!/usr/bin/env python3

from slugify import slugify
from assistant.common import logger
from assistant.commands.blog import web_scraper

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

    image = web_scraper.get_image_author(img_url, file_name)
    logger.info(is_verbose, 'Image url: %s' % image.url)
    logger.info(is_verbose, 'Image file name: %s' % image.file_name)
    logger.info(is_verbose, 'Image author: %s' % image.author_name)
    logger.info(is_verbose, 'Image author profile: %s' % image.author_profile)

    return 'Request: Successfully aquired image data from %s' % img_url