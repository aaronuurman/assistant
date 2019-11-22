#!/usr/bin/env python3

import unittest
from assistant.commands.blog.tasks.validate_image import ValidateImage

class TestValidateImage(unittest.TestCase):
  def test_empty_string_validate_img_error(self):
    #Arrange
    img = ''
    task = ValidateImage(img)
    #Act
    with self.assertRaises(ValueError) as value_error:
      task.execute()

    exception_message = value_error.exception.args[0]
    #Assert
    self.assertEqual('Blog image is required, currently supporting only Unsplash.', exception_message)

  def test_invalid_url_format_validate_img_error(self):
    #Arrange
    img = 'https://www'
    task = ValidateImage(img)
    #Act
    with self.assertRaises(ValueError) as value_error:
      task.execute()

    exception_message = value_error.exception.args[0]
    #Assert
    self.assertEqual('Invalid blog image url.', exception_message)

  def test_non_unsplash_url_validate_img_error(self):
    #Arrange
    img = 'https://www.test.com'
    task = ValidateImage(img)
    #Act
    with self.assertRaises(ValueError) as value_error:
      task.execute()

    exception_message = value_error.exception.args[0]
    #Assert
    self.assertEqual('Invalid blog image url, currently supporting only Unsplash images.', exception_message)

  def test_valid_url_validate_img_success(self):
    #Arrange
    img = 'https://unsplash.com/photos/OsF_qvHCoj0'
    task = ValidateImage(img)
    #Act
    result = task.execute()
    #Assert
    self.assertEqual('Validation: Image "https://unsplash.com/photos/OsF_qvHCoj0" is valid.', result)

if __name__ == '__main__':
  unittest.main()