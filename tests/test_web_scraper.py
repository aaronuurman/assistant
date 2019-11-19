#!/usr/bin/env python3

import unittest
from assistant import web_scraper
import tempfile, shutil, os

class TestWebScraper(unittest.TestCase):

  def test_unsplash_url_download_img_success(self):
    #Arrange
    image_path =  '/'.join(('/tmp', 'tempImg.jpg'))
    #Act
    web_scraper.download_img('https://unsplash.com/photos/AhC4pduPcGU', image_path)
    #Assert
    self.assertTrue(os.path.isfile(image_path))
    #CleanUp
    os.remove(image_path)

  def test_unsplash_url_get_image_author_success(self):
    #Arrange
    image_url = 'https://unsplash.com/photos/AhC4pduPcGU'
    image_file = 'tempImg.jpg'
    author = 'NOAA'
    author_profile = 'https://unsplash.com/@noaa'
    #Act
    image = web_scraper.get_image_author(image_url, image_file)
    #Assert
    self.assertEqual(image.author_name, author)
    self.assertEqual(image.author_profile, author_profile)
    self.assertEqual(image.file_name, image_file)
    self.assertEqual(image.url, image_url)

if __name__ == '__main__':
  unittest.main()