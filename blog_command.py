#!/usr/bin/env python3

from slugify import slugify
from os import path
import logger
import validator
import web_scraper
import file_handler

def handle(config, title, img_url, project_path):
	try:
		logger.info(config.verbose, 'Starting title validation.')
		title_validation_result = validator.validate_tile(title)
		logger.success(title_validation_result)

		logger.info(config.verbose, 'Starting image url validation.')
		img_validation_result = validator.validate_img(img_url)
		logger.success(img_validation_result)

		logger.info(config.verbose, 'Starting project path validation.')
		path_validation_result = validator.validate_project_path(project_path)
		logger.success(path_validation_result)

		logger.info(config.verbose, 'Requesting image data.')
		file_name = '.'.join((slugify(title),'jpg'))
		image = web_scraper.get_image_author(img_url, file_name)
		logger.info(config.verbose, 'Image url: %s' % image.url)
		logger.info(config.verbose, 'Image file name: %s' % image.file_name)
		logger.info(config.verbose, 'Image author: %s' % image.author_name)
		logger.info(config.verbose, 'Image author profile: %s' % image.author_profile)
		logger.success('Successfully aquired image data.')

		logger.info(config.verbose, 'Starting image download.')
		full_file_path = path.join(file_handler.find_sub_folder(project_path, '/src/images'), file_name)
		web_scraper.download_img(img_url, full_file_path)
		logger.success('Image "%s" downloaded succesfully to "%s".' % (img_url, full_file_path))

	except ValueError as er:
		logger.error('Validation Error: {}'.format(er))
	except Exception as ex:
		logger.error(format(ex))
