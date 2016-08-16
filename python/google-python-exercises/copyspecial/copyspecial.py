#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dirname):
  files_absolute = []
  filenames = os.listdir(dirname)
  for filename in filenames:
    match = re.search(r'__\w+__', filename)
    if match:
      filename_path = os.path.join(dirname, filename)
      filename_abs_path = os.path.abspath(filename_path)
      files_absolute.append(filename_abs_path)

  return files_absolute

def copy_to(paths, dirname):
  dest = os.path.abspath(dirname)
  if not os.path.exists(dest):
    os.makedirs(dest)

  for path in paths:
    shutil.copy(path, dest)

def zip_to(paths, zipfile):
  zip_cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
  (status, output) = commands.getstatusoutput(zip_cmd)
  if status:
    sys.stderr.write('zip error status: ' + str(status) + '\n')
    sys.stderr.write(output + '\n')
    sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
  all_special_files = []
  for arg in args:
    all_special_files += get_special_paths(arg)
   
  #check for duplicates
  base_names = []
  for special_file in all_special_files:
    base_name = os.path.basename(special_file)
    if base_name in base_names:
      sys.stderr.write('filename: ' + base_name + ' already exist!\n')
      sys.exit(1)
    else:
      base_names.append(base_name)

  if todir:
    copy_to(all_special_files, todir)
  elif tozip:
    zip_to(all_special_files, tozip)
  else:
    for special_file in all_special_files:
      print special_file

if __name__ == "__main__":
  main()
