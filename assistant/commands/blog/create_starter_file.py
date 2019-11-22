#!/usr/bin/env python3

from os import path
from slugify import slugify
from assistant.common import file_handler

class CreateStarterFile:
	def __init__(self, title, project_path):
		self.start_message = 'Preparing data for new post.'
		self.__title = title
		self.__project_path = project_path
		self.__file_name = '.'.join((slugify(title),'md'))

	def __template(self, image):
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
	""" % (self.__title, image.file_name, image.author_name, image.author_profile)

		return data

	def execute(self, image):
		full_post_path = path.join(file_handler.find_sub_folder(self.__project_path, '/src/pages/posts'), self.__file_name)
		post_data = self.__template(image)
		file_handler.write_to_file(full_post_path, post_data)

		return 'File: Blog starter file created to "%s"' % full_post_path