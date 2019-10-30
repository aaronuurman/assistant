#!/usr/bin/env python3

from str_helper import is_null_or_whitespace

def validate_tile(title):
  """Validate blog title.
  - required
  - at least 3 characters

  returns:
    Validation success message.
  """
  if is_null_or_whitespace(title):
    raise ValueError('Blog title is required, min-lenght 3 characters.')

  if (len(title) < 3):
    raise ValueError('Blog title must be at least 3 characters.')

  return 'Validation Success: Title "%s" is valid.' % title
