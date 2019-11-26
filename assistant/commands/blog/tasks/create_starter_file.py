#!/usr/bin/env python3

from os import path
from slugify import slugify
from datetime import datetime
from assistant.common import file_handler

class CreateStarterFile:
	def __init__(self, title, project_path):
		self.start_message = 'Preparing data for new post.'
		self.__title = title
		self.__project_path = project_path
		self.__date = datetime.now().strftime('%Y-%m-%d')
		self.__date_time = datetime.now().strftime('%Y-%m-%d %H:%M')
		self.__file_name = '.'.join(('%s-%s' % (self.__date,slugify(title)),'md'))

	def __template(self, image):
		"""Creates a blog starter template with filled data."""

		data = """---
title: %s
date: "%s"
image: '../../images/%s'
imageAuthor: ['%s', '%s']
imageProvider: ['Unsplash', 'https://unsplash.com']
tags:
- example
resources: [
	['https://www.example.com', 'Example']
]
---
	""" % (self.__title, self.__date_time, image.file_name, image.author_name, image.author_profile)

		return data

	def execute(self, image):
		full_post_path = path.join(file_handler.find_sub_folder(self.__project_path, '/src/pages/posts'), self.__file_name)
		post_data = self.__template(image)
		file_handler.write_to_file(full_post_path, post_data)

		return 'File creation: Starter file for blog post created to "%s"' % full_post_path