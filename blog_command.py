#!/usr/bin/env python3

from slugify import slugify
from os import path
import logger
import validator
import web_scraper
import file_handler
import git_handler

def handle(config, title, img_url, project_path):
	try:
		logger.info(config.verbose, 'Starting project path validation.')
		path_validation_result = validator.validate_project_path(project_path)
		logger.success(path_validation_result)

		logger.info(config.verbose, 'Starting title validation.')
		title_validation_result = validator.validate_tile(title)
		logger.success(title_validation_result)

		logger.info(config.verbose, 'Starting image url validation.')
		img_validation_result = validator.validate_img(img_url)
		logger.success(img_validation_result)

		logger.info(config.verbose, 'Requesting image data.')
		slug = slugify(title)
		image_file_name = '.'.join((slug,'jpg'))
		image = web_scraper.get_image_author(img_url, image_file_name)
		logger.info(config.verbose, 'Image url: %s' % image.url)
		logger.info(config.verbose, 'Image file name: %s' % image.file_name)
		logger.info(config.verbose, 'Image author: %s' % image.author_name)
		logger.info(config.verbose, 'Image author profile: %s' % image.author_profile)
		logger.success('Successfully aquired image data.')

		branch_name = git_handler.createNewBranch(slug)
		logger.success('Successfully created a new working branch "%s".' % branch_name)

		logger.info(config.verbose, 'Starting image download.')
		full_image_path = path.join(file_handler.find_sub_folder(project_path, '/src/images'), image_file_name)
		web_scraper.download_img(img_url, full_image_path)
		logger.success('Image "%s" downloaded succesfully to "%s".' % (img_url, full_image_path))
		
		logger.info(config.verbose, 'Preparing data for new post.')
		post_file_name = '.'.join((slug,'md'))
		full_post_path = path.join(file_handler.find_sub_folder(project_path, '/src/pages/posts'), post_file_name)
		post_data = __template(title, image.file_name, image.author_name, image.author_profile)
		file_handler.write_to_file(full_post_path, post_data)

	except ValueError as er:
		logger.error('Validation Error: {}'.format(er))
	except Exception as ex:
		logger.error(format(ex))


def __template(title, image, image_author, image_author_profile):
	"""Returns a blog starter template with filled data."""
	
	data = """---
title: %s
date: "2019-11-14 07:20"
image: '../../images/%s'
imageAuthor: ['%s', '%s']
imageProvider: ['Unsplash', 'https://unsplash.com']
tags:
- example
resources: [
	['https://www.example.com', 'Example']
]
---
	""" % (title, image, image_author, image_author_profile)

	return data