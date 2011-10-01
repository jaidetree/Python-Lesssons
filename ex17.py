from sys import argv
from shutil import copyfile

script, from_file, to_file = argv


copyfile( from_file, to_file )


