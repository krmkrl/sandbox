#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  puzzle_urls = []
  separator = filename.find('_') + 1
  hostname = filename[separator:]
  try:
    f = open(filename, 'rU')
    log_content = f.read()
    f.close()
  except IOError, e:
    sys.stderr.write('Cannot read from file ' + filename + '\n')
    sys.stderr.write(str(e))

  get_matches = re.findall(r'GET\s(\S+)', log_content)
  for get_match in get_matches:
    if 'puzzle' in get_match:
      #construct url using hostname from logfile
      url = 'http://' + hostname + get_match
      if url not in puzzle_urls:
        puzzle_urls.append(url)
      
  return sorted(puzzle_urls)
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  dir_path = os.path.abspath(dest_dir)
  if not os.path.exists(dir_path):
    os.makedirs(dir_path)

  count = 0
  images = []
  for img_url in img_urls:
    destfilename = 'img' + str(count)
    count += 1
    destpath = os.path.join(dir_path, destfilename)
    images.append(destpath)
    try:
      print 'Retrieving file', img_url, '...'
      urllib.urlretrieve(img_url, destpath)
    except IOError:
      sys.stderr.write('Problem retreiving url: ' + img_url)
      sys.exit(1)

  #create index.html
  f = open(os.path.join(dir_path, 'index.html'),'w')
  f.write('<verbatim>\n<html>\n<body>\n')
  for image in images:
    f.write('<img src="' + image + '">')
  f.write('</body>\n</html>\n')
  f.close()

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
