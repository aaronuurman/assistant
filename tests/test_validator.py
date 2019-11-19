#!/usr/bin/env python3

import unittest
from assistant.commands.blog import validator

class TestValidator(unittest.TestCase):
  
  def test_empty_string_validate_title_error(self):
    #Arrange
    title = ''
    #Act
    with self.assertRaises(ValueError) as value_error:
      validator.validate_tile(title)

    exception_message = value_error.exception.args[0]
    #Assert
    self.assertEqual('Blog title is required, min-lenght 3 characters.', exception_message)

  def test_short_string_validate_title_error(self):
    #Arrange
    title = 'te'
    #Act
    with self.assertRaises(ValueError) as value_error:
      validator.validate_tile(title)

    exception_message = value_error.exception.args[0]
    #Assert
    self.assertEqual('Blog title must be at least 3 characters.', exception_message)

  def test_string_validate_title_success(self):
    #Arrange
    title = 'test'
    #Act
    result = validator.validate_tile(title)
    #Assert
    self.assertEqual('Validation Success: Title "test" is valid.', result)

  def test_empty_string_validate_img_error(self):
    #Arrange
    img = ''
    #Act
    with self.assertRaises(ValueError) as value_error:
      validator.validate_img(img)

    exception_message = value_error.exception.args[0]
    #Assert
    self.assertEqual('Blog image is required, currently supporting only Unsplash.', exception_message)

  def test_invalid_url_format_validate_img_error(self):
    #Arrange
    img = 'https://www'
    #Act
    with self.assertRaises(ValueError) as value_error:
      validator.validate_img(img)

    exception_message = value_error.exception.args[0]
    #Assert
    self.assertEqual('Invalid blog image url.', exception_message)

  def test_non_unsplash_url_validate_img_error(self):
    #Arrange
    img = 'https://www.test.com'
    #Act
    with self.assertRaises(ValueError) as value_error:
      validator.validate_img(img)

    exception_message = value_error.exception.args[0]
    #Assert
    self.assertEqual('Invalid blog image url, currently supporting only Unsplash images.', exception_message)

  def test_valid_url_validate_img_success(self):
    #Arrange
    img = 'https://unsplash.com/photos/OsF_qvHCoj0'
    #Act
    result = validator.validate_img(img)
    #Assert
    self.assertEqual('Validation Success: Image "https://unsplash.com/photos/OsF_qvHCoj0" is valid.', result)

if __name__ == '__main__':
  unittest.main()