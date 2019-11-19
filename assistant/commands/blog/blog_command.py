#!/usr/bin/env python3

from os import path
from assistant.common import logger, file_handler
from assistant.commands.blog import web_scraper
from assistant.commands.blog.validate_image import ValidateImage
from assistant.commands.blog.validate_title import ValidateTitle
from assistant.commands.blog.reguest_img_data import RequestImageData
from assistant.commands.blog.create_new_branch import CreateNewBranch
from assistant.commands.blog.validate_project_path import ValidateProjectPath

def handle(config, title, img_url, project_path):
	try:
		tasks = [
			ValidateProjectPath(project_path),
			ValidateTitle(title),
			ValidateImage(img_url),
			RequestImageData(img_url, title, config),
			CreateNewBranch(title)
		]

		num_of_tasks = len(tasks)
		i = 1

		for task in tasks:
			logger.info(config.verbose, task.start_message)
			result = task.execute()
			message = "[%i/%i] %s" % (i, num_of_tasks, result)
			logger.success(message)
			i+=1

		# logger.info(config.verbose, 'Starting image download.')
		# full_image_path = path.join(file_handler.find_sub_folder(project_path, '/src/images'), image_file_name)
		# web_scraper.download_img(img_url, full_image_path)
		# logger.success('Image "%s" downloaded succesfully to "%s".' % (img_url, full_image_path))
		
		# logger.info(config.verbose, 'Preparing data for new post.')
		# post_file_name = '.'.join((slug,'md'))
		# full_post_path = path.join(file_handler.find_sub_folder(project_path, '/src/pages/posts'), post_file_name)
		# post_data = __template(title, image.file_name, image.author_name, image.author_profile)
		# file_handler.write_to_file(full_post_path, post_data)

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