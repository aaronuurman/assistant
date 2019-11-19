#!/usr/bin/env python3

import unittest
from assistant.commands.blog.validate_image import ValidateImage
from assistant.commands.blog.validate_title import ValidateTitle
from assistant.commands.blog.validate_project_path import ValidateProjectPath

class TestValidation(unittest.TestCase):
  
  def test_empty_string_validate_title_error(self):
    #Arrange
    title = ''
    task = ValidateTitle(title)
    #Act
    with self.assertRaises(ValueError) as value_error:
      task.execute()

    exception_message = value_error.exception.args[0]
    #Assert
    self.assertEqual('Blog title is required, min-lenght 3 characters.', exception_message)

  def test_short_string_validate_title_error(self):
    #Arrange
    title = 'te'
    task = ValidateTitle(title)
    #Act
    with self.assertRaises(ValueError) as value_error:
      task.execute()

    exception_message = value_error.exception.args[0]
    #Assert
    self.assertEqual('Blog title must be at least 3 characters.', exception_message)

  def test_string_validate_title_success(self):
    #Arrange
    title = 'test'
    task = ValidateTitle(title)
    #Act
    result = task.execute()
    #Assert
    self.assertEqual('Validation: Title "test" is valid.', result)

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