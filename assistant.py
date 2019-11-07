#!/usr/bin/env python3

import click
import logger
import validator

class Config(object):

	def __init__(self):
		self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option(
	'-v',
	'--verbose',
	is_flag=True,
	help='Will print verbose messages about processes.'
)
@pass_config
def cli(config, verbose):
	config.verbose = verbose

@cli.command()
@click.argument('title')
@click.argument('img')
@pass_config
def blog(config, title, img):
	"""Use this command to interact with blog."""
	try:
		logger.info(config.verbose, 'Starting title validation.')
		title_validation_result = validator.validate_tile(title)
		logger.success(title_validation_result)

		logger.info(config.verbose, 'Starting img validation.')
		img_validation_result = validator.validate_img(img)
		logger.success(img_validation_result)
	except ValueError as er:
		logger.error('Validation Error: {}'.format(er))
	except Exception as ex:
		logger.error(format(ex))

# Add blog command to cli
cli.add_command(blog)
