#!/usr/bin/env python3

from assistant.common import logger
from assistant.commands.blog.tasks.download_img import DownloadImg
from assistant.commands.blog.tasks.validate_image import ValidateImage
from assistant.commands.blog.tasks.validate_title import ValidateTitle
from assistant.commands.blog.tasks.reguest_img_data import RequestImageData
from assistant.commands.blog.tasks.create_new_branch import CreateNewBranch
from assistant.commands.blog.tasks.create_starter_file import CreateStarterFile
from assistant.commands.blog.tasks.commit_push_changes import CommitPushChanges
from assistant.commands.blog.tasks.validate_project_path import ValidateProjectPath

def handle(config, title, img_url, project_path):
	try:
		image = {}
		tasks = [
			ValidateProjectPath(project_path),
			ValidateTitle(title),
			ValidateImage(img_url),
			RequestImageData(img_url, title, config),
			CreateNewBranch(title, project_path),
			DownloadImg(project_path, img_url, title),
			CreateStarterFile(title, project_path),
			CommitPushChanges(project_path, title)
		]

		num_of_tasks = len(tasks)
		i = 1

		for task in tasks:
			logger.info(config.verbose, task.start_message)
			
			# RequestImageData returns multiple result and image object.
			# Image object is later used for creating a template.
			if (type(task).__name__ == 'RequestImageData'):
				result, image = task.execute()
			elif (type(task).__name__ == 'CreateStarterFile'):
				result = task.execute(image)
			else:
				result = task.execute()

			message = "[%i/%i] %s" % (i, num_of_tasks, result)
			logger.success(message)
			i+=1

	except ValueError as er:
		logger.error('Validation Error: {}'.format(er))
	except Exception as ex:
		logger.error(format(ex))