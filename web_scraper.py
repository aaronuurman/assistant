#!/usr/bin/env python3

from urllib import request, parse
from bs4 import BeautifulSoup

class Image:

  def __init__(self, file_name, url, author_name, author_profile):
    self.file_name = file_name
    self.url = url
    self.author_name = author_name
    self.author_profile = author_profile

def download_img(imageUrl, filePath):
  """Download image from Unsplash and save it in provided location"""

  downloadEndPoint = imageUrl + '/download?force=true'
  request.urlretrieve(downloadEndPoint, filePath)

def get_image_author(imageUrl, file_name):
  """Request image author data from page.
  
  Returns Image object with filled data.
  """

  selector = '_3XzpS _1ByhS _4kjHg _1O9Y0 _3l__V _1CBrG xLon9'
  response = request.urlopen(imageUrl)

  if response.code != 200:
    raise Exception('Failed to make request to "%s"' % imageUrl)

  data = response.read()
  html = data.decode('UTF-8')
  soup = BeautifulSoup(html, "html.parser")
  anchor = soup.find('a', class_=selector)
  username = anchor['href'].lstrip('/')
  author = anchor.contents[0]
  parsed_uri = parse.urlparse(imageUrl)
  author_profile = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
  image = Image(file_name, imageUrl, author, (author_profile + username))

  return image
