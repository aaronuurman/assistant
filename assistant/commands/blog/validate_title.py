#!/usr/bin/env python3

from assistant.common.str_helper import is_null_or_whitespace

class ValidateTitle:
  def __init__(self, title):
    self.start_message = 'Starting title validation.'
    self.__title = title
  
  def execute(self):
    """Validate blog title.
    - required
    - at least 3 characters

    returns:
      Validation success message.
    """
    title = self.__title

    if is_null_or_whitespace(title):
      raise ValueError('Blog title is required, min-lenght 3 characters.')

    if (len(title) < 3):
      raise ValueError('Blog title must be at least 3 characters.')

    return 'Validation: Title "%s" is valid.' % title