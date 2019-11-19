#!/usr/bin/env python3

import unittest
from assistant import str_helper

class TestStrHelper(unittest.TestCase):
  
  def test_empty_string_is_null_or_whitespace_true(self):
    #Arrange
    text = ''
    #Act
    result = str_helper.is_null_or_whitespace(text)
    #Assert
    self.assertTrue(result)

  def test_whitespace_is_null_or_whitespace_true(self):
    #Arrange
    text = ' '
    #Act
    result = str_helper.is_null_or_whitespace(text)
    #Assert
    self.assertTrue(result)

  def test_string_is_null_or_whitespace_false(self):
    #Arrange
    text = 'Some test string'
    #Act
    result = str_helper.is_null_or_whitespace(text)
    #Assert
    self.assertFalse(result)
  
if __name__ == '__main__':
  unittest.main()