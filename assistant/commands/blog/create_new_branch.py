#!/usr/bin/env python3

import os
from slugify import slugify

class CreateNewBranch:
  def __init__(self, title):
    self.start_message = 'Starting new git branch creation.'
    self.__branch_name = 'post-%s' % slugify(title)

  def execute(self):
    command = 'git checkout -B ' + self.__branch_name
    os.system(command)
    
    return 'Git: Created a new working branch "%s".' % self.__branch_name