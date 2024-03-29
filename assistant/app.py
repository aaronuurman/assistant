#!/usr/bin/env python3

import click, os
from assistant.commands.blog import blog_command
from assistant.common.str_helper import is_null_or_whitespace
from assistant.dto.config_dto import ConfigDto

pass_config = click.make_pass_decorator(ConfigDto, ensure=True)

# App entrypoint
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

# Blog command
@cli.command()
@click.option(
	'-t',
	'--title',
	required=True,
	type=str,
	help='The title of blog post.'
)
@click.option(
	'-i',
	'--image',
	required=True,
	type=str,
	help='The Unsplash image url.'
)
@click.option(
	'-p',
	'--project-path',
	required=False,
	type=click.Path(),
	help='The full path to project folder. Default: current working directory.',
	default=os.getcwd()
)
@pass_config
def blog(config, title, image, project_path):
	"""Use this command to start a new blog post."""

	blog_command.handle(config, title, image, project_path)

# Add blog command to cli
cli.add_command(blog)