#!/usr/bin/env python3

from str_helper import is_null_or_whitespace
import re

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

def validate_img(img):
  """Validate blog image.
  - required
  - starts with https
  - is a unsplash link

  returns:
    Validation success message.
  """
  if is_null_or_whitespace(img):
    raise ValueError('Blog image is required, currently supporting only Unsplash.')
  
  regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

  result = re.match(regex, img)

  if result is None :
    raise ValueError('Blog image url is not a valid URL.')

  return 'Validation Success: Image "%s" is valid.' % img