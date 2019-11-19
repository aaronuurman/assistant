#!/usr/bin/env python3

import re
from assistant.common.str_helper import is_null_or_whitespace

class ValidateImage:
  def __init__(self, img):
    self.start_message = 'Starting image url validation.'
    self.__img = img

  def execute(self):
    """Validate blog image.
    - required
    - starts with https
    - is a unsplash link

    returns:
      Validation success message.
    """
    img = self.__img

    if is_null_or_whitespace(img):
      raise ValueError('Blog image is required, currently supporting only Unsplash.')

    regex = re.compile(
          r'^(?:http|ftp)s?://' # http:// or https://
          r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
          r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
          r'(?::\d+)?' # optional port
          r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    result = re.match(regex, img)

    if result is None :
      raise ValueError('Invalid blog image url.')

    if "unsplash.com/photos/" not in img:
      raise ValueError('Invalid blog image url, currently supporting only Unsplash images.')

    return 'Validation: Image "%s" is valid.' % img