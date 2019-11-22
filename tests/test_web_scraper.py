#!/usr/bin/env python3

import unittest
import tempfile, shutil, os
from assistant.commands.blog import web_scraper
from assistant.commands.blog.tasks.download_img import DownloadImg

class TestWebScraper(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    os.mkdir('/tmp/blog')
    os.mkdir('/tmp/blog/src')
    os.mkdir('/tmp/blog/src/images')

  def test_unsplash_url_download_img_success(self):
    #Arrange
    project_path = '/tmp/blog'
    image_url = 'https://unsplash.com/photos/AhC4pduPcGU'
    title = 'Temporary Testing'
    downloadTask = DownloadImg(project_path, image_url, title)
    #Act
    downloadTask.execute()
    #Assert
    self.assertTrue(os.path.isfile('/tmp/blog/src/images/temporary-testing.jpg'))

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

  @classmethod
  def tearDownClass(cls):
    shutil.rmtree('/tmp/blog')

if __name__ == '__main__':
  unittest.main()