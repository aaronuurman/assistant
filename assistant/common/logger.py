#!/usr/bin/env python3

from click import echo, style

def info(isVerbose, text):
  """Log information to the command line if verbose is enabled."""
  if isVerbose:
    echo(text)

def error(text):
  """Log error message to the command line."""
  echo(style(text, fg='red'))

def success(text):
  """Log success message to command line."""
  echo(style(text, fg='green'))  