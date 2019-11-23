#!/usr/bin/env python3

import unittest
from assistant.commands.blog.tasks.validate_title import ValidateTitle

class TestValidateTitle(unittest.TestCase):
	
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

if __name__ == '__main__':
	unittest.main()